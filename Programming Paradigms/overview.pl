#!/usr/bin/perl
use warnings;
use strict;

# check whether the command line contains two parameters
if ($#ARGV != 1){
	die "Your command line should contains 2 arguments, such as overview.pl DIRECTORY NAMEPATTERN* or overview.pl DIRECTORY *NAMEPATTERN";
}

#check whether folder exist
if (! -d $ARGV[0])
{
	die "the directory, $ARGV[0], cannot find, Please input the correct directory";
}

# two different way to input the "NAMEPATTERN", such as "NAMEPATTERN*" or "*NAMEPATTERN"

my $filename='tmp';
open(my $fh, '>', $filename) or die "Could not open file $filename $!";
my $file = `find ./$ARGV[0] -name "$ARGV[1]" -type f -exec du -ch {} +`;

# hold the file name, location, size as a list

my @tmp_list=split(/[\t+,\n]/, $file);
my $list_size=@tmp_list;


print $fh "$file";
close $fh;

# seperate a list as a location list and a size list and a file name list
my @location_list;
my @size_list;
my @filename;
for(my $x=2; $x<$list_size-2; $x++){
	if (0==$x%2){
		push @size_list,"$tmp_list[$x]";
	}else{
# input: location list ---> output: a file name list and a location list
		#print("$tmp_list[$x]\n");
		$tmp_list[$x]=~ s/.//;
		push @location_list, "$tmp_list[$x]";
		#print("@location_list\n");
		$tmp_list[$x]=~ m|/([^/.]*\.[^/.]*)$|;
		#print("$tmp_list[$x]\n");
		push @filename,"$1";
}
}





# hold  ownership 
my @ownership;

for (my $i=0; $i<scalar(@filename); $i++){
	my $awk=q(awk '{print $3}');
	my $tmp_owner=`ls -l $ARGV[0]/$filename[$i] | $awk`;
#	print("$filename[$i]\n");
	#print("$tmp_owner\n");
#print("$tmp_owner\n");
	#print(" $owner[2]\n");
	push @ownership,"$tmp_owner";
}


#create the image "gnuplot.jpg"

`cat << __EOF | gnuplot
set style data histogram
set style fill solid 0.5 border -1
set term png
set output "gnuplot.png"
set title "./$ARGV[0]"
plot 'tmp' with impulses lw 9
__EOF`;

#create the overview.html


open (my $html, ">overview.html") or die "can't open out";
#create the html path
my $html_path=`pwd`;
my $table;
for (my $i=0; $i<scalar(@filename); $i++){
	my $table_tmp="<tr>
	<td align=\"center\"><a href=\"$html_path$location_list[$i]\" target=\"_blank\">$filename[$i]</a></td>
	<td align=\"center\">$location_list[$i]</td>
	<td align=\"center\">$size_list[$i]</td>
	<td align=\"center\">$ownership[$i]</td>
	</tr>
	";
	$table .=$table_tmp
}


my $template="<html>
<head>
<title>$ARGV[0]</title>
</head>
<body>
<h2>List of Files</h2>
<table style=\"width:100%\">
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



