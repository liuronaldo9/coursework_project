#!/usr/bin/perl
use warnings;
use strict;

# check whether the command line contains two parameters
if ($#ARGV != 1){
	die "Your command line should contains 2 arguments, such as overview.pl DIRECTORY NAMEPATTERN* or overview.pl DIRECTORY *NAMEPATTERN";
}

#check whether folder exist, please write absolute path, for example /home/c1749059/perl, or /bin
if (! -d $ARGV[0])
{
	die "the directory, $ARGV[0], cannot find, Please input the correct directory, please write absolute path";
}

# two different way to input the "NAMEPATTERN", such as "NAMEPATTERN*" or "*NAMEPATTERN"
# such as "*lab" or "lab*"
# the temportry file has been save in location /tmp/temp_data
my $filename='/tmp/temp_data';
my @tmp_list;
my $list_size;
# use command such as  "find /bin -name "l*" -type f -exec du -c {} + | sort -n" for saving the size and location of file
open(my $fh, '>', $filename) or die "Could not open file $filename $!";
my $file = `find $ARGV[0] -name "$ARGV[1]" -type f -exec du -c {} + | sort -n `;

# separated the original string to list through tab, it will help get size and location and file at next stage.
@tmp_list=split(/[\t+,\n]/, $file);
$list_size=@tmp_list;


print $fh "$file";
close $fh;

# For example, "*l", which means l at the end of the file name, or "l*", which means l at the beginning of the string, or you can input the specific filename.

if ($list_size == 0){
	die "we cannot find your file, Please check your filename and change your requirment"
}

# seperate a list as a location list and a size list and a file name list. From here, the programing will save the location and size and filename as list, they will use in table in HTML file.
my @location_list;
my @size_list;
my @filename;
for(my $x=0; $x<$list_size-2; $x++){
	if (0==$x%2){
		push @size_list,"$tmp_list[$x]";
	}else{
# input: location list ---> output: a file name list and a location list
		push @location_list, "$tmp_list[$x]";
		# location will be seperated and get the last element from list. it will get the file name
		my @temp_file=split(/\//, $tmp_list[$x]);
		my $tempfilename=@temp_file;
		$tmp_list[$x]=$temp_file[$tempfilename-1];
		push @filename,"$tmp_list[$x]";
	}
}



# hold  ownership , we use ls -l "location" | awk '{print $3}' for getting ownership, we also can get file size from here.
my @ownership;

for (my $i=0; $i<scalar(@filename); $i++){
	my $awk=q(awk '{print $3}');
	my $tmp_owner=`ls -l $location_list[$i] | $awk`;
	push @ownership,"$tmp_owner";
}



#create the image "gnuplot.jpg"
# the graph with impulses and linewidth is 9.

`cat << __EOF | gnuplot
set style data histogram
set style fill solid 0.5 border -1
set xtics border in scale 0,0 nomirror rotate by -90  autojustify
set term png size 1800, 1000
set offset 0.2,0
set output "gnuplot.png"
set title "$ARGV[0]"
plot '/tmp/temp_data' using 1:xtic(2) with impulses lw 9
__EOF`;

#create the overview.html

open (my $html, ">overview.html") or die "can't open out";
#create the html path, it will help us find the image location, because its location may change.
my $html_path=`pwd`;
my $table;
for (my $i=0; $i<scalar(@filename); $i++){
	my $table_tmp="<tr>
	<td align=\"center\"><a href=\"$location_list[$i]\" target=\"_blank\">$filename[$i]</a></td>
	<td align=\"center\">$location_list[$i]</td>
	<td align=\"center\">$size_list[$i]</td>
	<td align=\"center\">$ownership[$i]</td>
	</tr>
	";
	$table .=$table_tmp
}

# create the HTML template
my $template="<html>
<head>
<title>$ARGV[0]</title>
</head>
<body>
<h2>List of Files</h2>
<table border=\"9\" style=\"width:100%\">
<tr>
<th>Files Name</th>
<th>Location</th>
<th>Size</th>
<th>Ownership</th>
</tr>
$table
</table>
<img src=\"file://$html_path/gnuplot.png\">
</body>
</html>
";
print $html "$template";
close  $html;

