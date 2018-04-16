#!/usr/bin/perl -w
use strict;
use warnings;
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

@tmp_list=split(/[\t+,\n]/, $file);
$list_size=@tmp_list;

while ($row=<>){
	if ($row=~ \t\./g){
		print ("$row\n")}
}
print $fh "$file";
close $fh;

# seperate a list as a location list and a size list and a file name list
@location_list;
@size_list;
@filename;
for($x=2; $x<$list_size-2; $x++){
	if (0==$x%2){
		push @size_list,"@list[$x]";
	}else{
# input: location list ---> output: a file name list and a location list
		@list[$x]=~ s/.//;
		push @location_list, "@list[$x]";
		@list[$x]=~ m|/([^/.]*\.[^/.]*)$|;
		push @filename,"$1";
}





# hold  ownership 



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
<img src=\"file://$html_path/gnuplot.png\">
</body>
</html>
";


print $html "$template";
close  $html;


=pod
	my $filename='tmp';
	open(my $fh, '>', $filename) or die "Could not open file$filename $!";
	my $file = `find ./$ARGV[0] -type f -exec du -ch {} +`;
	print $fh "$file";
	close $fh;
my $program = `cat << __EOF | gnuplot
set term canvas mousing size 500, 500
set output "gnuplot.html"
set title "./$ARGV[0]"
plot 'tmp' with impulses
__EOF`;

=cut

	#$orginal=exec($file);
#	print($file);


# analysis the 



#readlink -f "overview.pl"
#getfacl overview.pl
#check the ownership ls -l overview.pl
# du -ah --exclude="*.txt"


#foreach (@ARGV) {
#    print "$_\n";
#};
#$size=@ARGV;
#print("@ARGV[0]\n");
#print("$size\n");
#print("$#ARGV\n");

