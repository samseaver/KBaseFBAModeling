#!/usr/bin/env perl
########################################################################
# Authors: Christopher Henry, Scott Devoid, Paul Frybarger
# Contact email: chenry@mcs.anl.gov
# Development location: Mathematics and Computer Science Division, Argonne National Lab
########################################################################
use strict;
use warnings;
use Bio::KBase::workspace::ScriptHelpers qw(get_ws_client workspace workspaceURL parseObjectMeta parseWorkspaceMeta printObjectMeta);
use Bio::KBase::fbaModelServices::ScriptHelpers qw(fbaws get_fba_client runFBACommand universalFBAScriptCode );
#Defining globals describing behavior
my $primaryArgs = ["Phenotype simulation ID"];
my $servercommand = "export_phenotypeSimulationSet";
my $script = "fba-exportphenosim";
my $translation = {
	"Phenotype simulation ID" => "phenotypeSimulationSet",
	workspace => "workspace",
};
#Defining usage and options
my $specs = [
    [ 'workspace|w:s', 'Workspace with phenotype simulation set', { "default" => fbaws() } ]
];
my ($opt,$params) = universalFBAScriptCode($specs,$script,$primaryArgs,$translation);
#Calling the server
my $output = runFBACommand($params,$servercommand,$opt);
#Checking output and report results
if (!defined($output)) {
	print STDERR "Phenotype simulation set export failed!\n";
} else {
	print STDERR "Phenotype simulation set export succeeded:\n";
	print $output;
}