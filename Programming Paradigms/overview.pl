#!/usr/bin/perl -w
use strict;
use warnings;
# got the file information and keep in tmp file.
if ($#ARGV == 1){
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
}
	#$orginal=exec($file);
#	print($file);
else{
	print( "Your command line should contains 2 arguments, such as overview.pl DIRECTORY NAMEPATTERN*");}

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

