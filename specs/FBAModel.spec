/*
@author chenry
*/
module KBaseFBA {
    typedef int bool;
    /*
		Reference to a compound object
		@id subws KBaseBiochem.Biochemistry.compounds.[*].id
	*/
    typedef string compound_ref;
    /*
		Reference to a mapping object
		@id ws KBaseOntology.Mapping
	*/
    typedef string mapping_ref;
    /*
		Reference to a classifier object
		@id ws KBaseFBA.Classifier
	*/
    typedef string Classifier_ref;
    /*
		Reference to a training set object
		@id ws KBaseFBA.ClassifierTrainingSet
	*/
    typedef string Trainingset_ref;
    /*
		Reference to a biochemistry object
		@id ws KBaseBiochem.Biochemistry
	*/
    typedef string Biochemistry_ref;
    /*
		Template biomass ID
		@id external
	*/
    typedef string templatebiomass_id;
    /*
		Template biomass compound ID
		@id external
	*/
    typedef string templatebiomasscomponent_id;
	/*
		Template reaction ID
		@id external
	*/
    typedef string templatereaction_id;
    /*
		ModelTemplate ID
		@id kb
	*/
    typedef string modeltemplate_id;
    /*
		Reference to a model template
		@id ws KBaseBiochem.Media
	*/
    typedef string media_ref;
    /*
		Reference to a model template
		@id ws KBaseGenomes.Genome
	*/
    typedef string genome_ref;
    /*
		Reference to a model template
		@id ws KBaseFBA.ModelTemplate
	*/
    typedef string template_ref;
    /*
		Reference to an OTU in a metagenome
		@id subws KBaseGenomes.MetagenomeAnnotation.otus.[*].id
	*/
    typedef string metagenome_otu_ref;
    /*
		Reference to a metagenome object
		@id ws KBaseGenomes.MetagenomeAnnotation
	*/
    typedef string metagenome_ref;
    /*
		Reference to a feature of a genome object
		@id subws KBaseGenomes.Genome.features.[*].id
	*/
    typedef string feature_ref;
	/*
		Reference to a gapgen object
		@id ws KBaseFBA.Gapgeneration
	*/
    typedef string gapgen_ref;
    /*
		Reference to a FBA object
		@id ws KBaseFBA.FBA
	*/
    typedef string fba_ref;
	/*
		Reference to a gapfilling object
		@id ws KBaseFBA.Gapfilling
	*/
    typedef string gapfill_ref;
	/*
		Reference to a complex object
		@id subws KBaseOntology.Mapping.complexes.[*].id
	*/
    typedef string complex_ref;
	/*
		Reference to a reaction object in a biochemistry
		@id subws KBaseBiochem.Biochemistry.reactions.[*].id
	*/
    typedef string reaction_ref;
    /*
		Reference to a reaction object in a model
		@id subws KBaseFBA.FBAModel.modelreactions.[*].id
	*/
    typedef string modelreaction_ref;
    /*
		Reference to a biomass object in a model
		@id subws KBaseFBA.FBAModel.biomasses.[*].id
	*/
    typedef string biomass_ref;
	/*
		Reference to a compartment object in a model
		@id subws KBaseFBA.FBAModel.modelcompartments.[*].id
	*/
    typedef string modelcompartment_ref;
	/*
		Reference to a compartment object
		@id subws KBaseBiochem.Biochemistry.compartments.[*].id
	*/
    typedef string compartment_ref;
	/*
		Reference to a compound object in a model
		@id subws KBaseFBA.FBAModel.modelcompounds.[*].id
	*/
    typedef string modelcompound_ref;
    /*
		Reference to regulatory model
		@id ws KBaseRegulation.RegModel
	*/
    typedef string regmodel_ref;
    /*
		Reference to regulome
		@id ws KBaseRegulation.Regulome
	*/
    typedef string regulome_ref;
    /*
		Reference to PROM constraints
		@id ws KBaseFBA.PromConstraint
	*/
    typedef string promconstraint_ref;
    /*
		Reference to expression data
		@id ws KBaseExpression.ExpressionSeries
	*/
    typedef string expression_series_ref;
    /*
		Reference to expression data
		@id ws KBaseExpression.ExpressionSample
	*/
    typedef string expression_sample_ref;
    /*
		Reference to probabilistic annotation
		@id ws KBaseProbabilisticAnnotation.ProbAnno
	*/
    typedef string probanno_ref;
    /*
		Reference to a phenotype set object
		@id ws KBasePhenotypes.PhenotypeSet
	*/
    typedef string phenotypeset_ref;
    /*
		Reference to a phenotype simulation set object
		@id ws KBasePhenotypes.PhenotypeSimulationSet
	*/
    typedef string phenotypesimulationset_ref;
    /*
		Reference to metabolic model
		@id ws KBaseFBA.FBAModel
	*/
    typedef string fbamodel_ref;
	/*
		KBase genome ID
		@id kb
	*/
    typedef string genome_id;
    /*
		KBase FBA ID
		@id kb
	*/
    typedef string fba_id;
    /*
		Biomass reaction ID
		@id external
	*/
    typedef string biomass_id;
    /*
		Gapgeneration solution ID
		@id external
	*/
    typedef string gapgensol_id;
    /*
		Model compartment ID
		@id external
	*/
    typedef string modelcompartment_id;
    /*
		Model compound ID
		@id external
	*/
    typedef string modelcompound_id;
    /*
		Model reaction ID
		@id external
	*/
    typedef string modelreaction_id;
    /*
		Genome feature ID
		@id external
	*/
    typedef string feature_id;
    /*
		Source ID
		@id external
	*/
    typedef string source_id;
    /*
		Gapgen ID
		@id kb
	*/
    typedef string gapgen_id;
	/*
		Gapfill ID
		@id kb
	*/
    typedef string gapfill_id;
    /*
		Gapfill solution ID
		@id external
	*/
    typedef string gapfillsol_id;
    /*
		FBAModel ID
		@id kb
	*/
    typedef string fbamodel_id;
    /* 
    	BiomassCompound object
    	
		@searchable ws_subset modelcompound_ref coefficient
    */
    typedef structure {
		modelcompound_ref modelcompound_ref;
		float coefficient;
    } BiomassCompound;
    
    /* 
    	Biomass object
    */
    typedef structure {
		biomass_id id;
		string name;
		float other;
		float dna;
		float rna;
		float protein;
		float cellwall;
		float lipid;
		float cofactor;
		float energy;
		list<BiomassCompound> biomasscompounds;
    } Biomass;

    /* 
    	ModelCompartment object
    */
    typedef structure {
		modelcompartment_id id;
		compartment_ref compartment_ref;
		int compartmentIndex;
		string label;
		float pH;
		float potential;
    } ModelCompartment;
    
    /* 
    	ModelCompound object
    	
    	@optional aliases
    */
    typedef structure {
		modelcompound_id id;
		compound_ref compound_ref;
		list<string> aliases;
		string name;
		float charge;
		string formula;
		modelcompartment_ref modelcompartment_ref;
    } ModelCompound;
    
    /* 
    	ModelReactionReagent object
    	
		@searchable ws_subset modelcompound_ref coefficient
    */
    typedef structure {
		modelcompound_ref modelcompound_ref;
		float coefficient;
    } ModelReactionReagent;
    
    /* 
    	ModelReactionProteinSubunit object
    	
		@searchable ws_subset role triggering optionalSubunit feature_refs
    */
    typedef structure {
		string role;
		bool triggering;
		bool optionalSubunit;
		string note;
		list<feature_ref> feature_refs;
    } ModelReactionProteinSubunit;
    
    /* 
    	ModelReactionProtein object
    */
    typedef structure {
		complex_ref complex_ref;
		string note;
		list<ModelReactionProteinSubunit> modelReactionProteinSubunits;
    } ModelReactionProtein;
    
    /* 
    	ModelReaction object
    	
    	@optional name pathway reference aliases
    */
    typedef structure {
		modelreaction_id id;
		reaction_ref reaction_ref;
		string name;
		list<string> aliases;
		string pathway;
		string reference;
		string direction;
		float protons;
		modelcompartment_ref modelcompartment_ref;
		float probability;
		list<ModelReactionReagent> modelReactionReagents;
		list<ModelReactionProtein> modelReactionProteins;
    } ModelReaction;

    /* 
    	ModelGapfill object
    	 
    	@optional integrated_solution
    */
    typedef structure {
		gapfill_id id;
		gapfill_id gapfill_id;
		gapfill_ref gapfill_ref;
		bool integrated;
		string integrated_solution;
		media_ref media_ref;
    } ModelGapfill;
    
    /* 
    	ModelGapgen object
    	
    	@optional integrated_solution
    */
    typedef structure {
    	gapgen_id id;
    	gapgen_id gapgen_id;
		gapgen_ref gapgen_ref;
		bool integrated;
		string integrated_solution;
		media_ref media_ref;
    } ModelGapgen;
    
    /* 
    	FBAModel object
    	
    	@optional metagenome_otu_ref metagenome_ref genome_ref template_refs
    	@searchable ws_subset id source_id source name type genome_ref metagenome_ref metagenome_otu_ref template_ref
    */
    typedef structure {
		fbamodel_id id;
		string source;
		source_id source_id;
		string name;
		string type;
		genome_ref genome_ref;
		metagenome_ref metagenome_ref;
		metagenome_otu_ref metagenome_otu_ref;
		template_ref template_ref;
		
		list<template_ref> template_refs;
		list<ModelGapfill> gapfillings;
		list<ModelGapgen> gapgens;
		
		list<Biomass> biomasses;
		list<ModelCompartment> modelcompartments;
		list<ModelCompound> modelcompounds;
		list<ModelReaction> modelreactions;
    } FBAModel;
    
    /* 
    	FBAConstraint object
    */
    typedef structure {
    	string name;
    	float rhs;
    	string sign;
    	mapping<modelcompound_id,float> compound_terms;
    	mapping<modelreaction_id,float> reaction_terms;
    	mapping<biomass_id,float> biomass_terms;
	} FBAConstraint;
    
    /* 
    	FBAReactionBound object
    */
    typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
	} FBAReactionBound;
    
    /* 
    	FBACompoundBound object
    */
     typedef structure {
    	modelcompound_ref modelcompound_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
	} FBACompoundBound;
    
    /* 
    	FBACompoundVariable object
    */
    typedef structure {
    	modelcompound_ref modelcompound_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBACompoundVariable;
	
	/* 
    	FBAReactionVariable object
    */
	typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBAReactionVariable;
	
	/* 
    	FBABiomassVariable object
    */
	typedef structure {
    	biomass_ref biomass_ref;
    	string variableType;
    	float upperBound;
    	float lowerBound;
    	string class;
    	float min;
    	float max;
    	float value;
	} FBABiomassVariable;
	
	/* 
    	FBAPromResult object
    */
	typedef structure {
    	float objectFraction;
    	float alpha;
    	float beta;
	} FBAPromResult;
    

	/*
	  Either of two values: 
	   - InactiveOn: specified as on, but turns out as inactive
	   - ActiveOff: specified as off, but turns out as active
	 */
	typedef string conflict_state;
	/*
	  FBATintleResult object	 
	*/
	typedef structure {
		float originalGrowth;
		float growth;
		float originalObjective;
		float objective;
		mapping<conflict_state,feature_id> conflicts;		    
	} FBATintleResult;

    /* 
    	FBADeletionResult object
    */
    typedef structure {
    	list<feature_ref> feature_refs;
    	float growthFraction;
	} FBADeletionResult;
	
	/* 
    	FBAMinimalMediaResult object
    */
	typedef structure {
    	list<compound_ref> essentialNutrient_refs;
    	list<compound_ref> optionalNutrient_refs;
	} FBAMinimalMediaResult;
    
    /* 
    	FBAMetaboliteProductionResult object
    */
    typedef structure {
    	modelcompound_ref modelcompound_ref;
    	float maximumProduction;
	} FBAMetaboliteProductionResult;
    
	/* 
    	FBAMinimalReactionsResult object
    */
    typedef structure {
    	string id;
    	bool suboptimal;
    	float totalcost;
    	list<modelreaction_ref> reaction_refs;
    	list<string> reaction_directions;
	} FBAMinimalReactionsResult;  
    

    typedef float probability;
    /*
      collection of tintle probability scores for each feature in a genome,
      representing a single gene probability sample
    */
    typedef structure {
	    mapping<feature_id,probability> tintle_probability;
	    string expression_sample_ref;	    
    } TintleProbabilitySample;

    /* 
    	FBA object holds the formulation and results of a flux balance analysis study
    	
    	@optional minimize_reactions minimize_reaction_costs FBATintleResults FBAMinimalReactionsResults PROMKappa phenotypesimulationset_ref objectiveValue phenotypeset_ref promconstraint_ref regmodel_ref tintlesample_ref tintleW tintleKappa
    	@searchable ws_subset comboDeletions id fva fluxMinimization findMinimalMedia allReversible simpleThermoConstraints thermodynamicConstraints noErrorThermodynamicConstraints minimizeErrorThermodynamicConstraints
    	@searchable ws_subset regmodel_ref fbamodel_ref promconstraint_ref media_ref phenotypeset_ref geneKO_refs reactionKO_refs additionalCpd_refs objectiveValue phenotypesimulationset_ref
    */
    typedef structure {
		fba_id id;
		bool fva;
		bool fluxMinimization;
		bool findMinimalMedia;
		bool allReversible;
		bool simpleThermoConstraints;
		bool thermodynamicConstraints;
		bool noErrorThermodynamicConstraints;
		bool minimizeErrorThermodynamicConstraints;
		
		bool maximizeObjective;
		mapping<modelcompound_id,float> compoundflux_objterms;
    	mapping<modelreaction_id,float> reactionflux_objterms;
		mapping<biomass_id,float> biomassflux_objterms;
		
		int comboDeletions;
		int numberOfSolutions;
		
		float objectiveConstraintFraction;
		float defaultMaxFlux;
		float defaultMaxDrainFlux;
		float defaultMinDrainFlux;
		float PROMKappa;
		float tintleW;
		float tintleKappa;
		
		bool decomposeReversibleFlux;
		bool decomposeReversibleDrainFlux;
		bool fluxUseVariables;
		bool drainfluxUseVariables;
		bool minimize_reactions;
		
		regmodel_ref regmodel_ref;
		fbamodel_ref fbamodel_ref;
		promconstraint_ref promconstraint_ref;
		expression_sample_ref tintlesample_ref;
		media_ref media_ref;
		phenotypeset_ref phenotypeset_ref;
		list<feature_ref> geneKO_refs;
		list<modelreaction_ref> reactionKO_refs;
		list<modelcompound_ref> additionalCpd_refs;
		mapping<string,float> uptakeLimits;
		mapping<modelreaction_id,float> minimize_reaction_costs;
		
		mapping<string,string> parameters;
		mapping<string,list<string>> inputfiles;
		
		list<FBAConstraint> FBAConstraints;
		list<FBAReactionBound> FBAReactionBounds;
		list<FBACompoundBound> FBACompoundBounds;
			
		float objectiveValue;
		mapping<string,list<string>> outputfiles;
		phenotypesimulationset_ref phenotypesimulationset_ref;

		list<FBACompoundVariable> FBACompoundVariables;
		list<FBAReactionVariable> FBAReactionVariables;
		list<FBABiomassVariable> FBABiomassVariables;
		list<FBAPromResult> FBAPromResults;
		list<FBATintleResult> FBATintleResults;
		list<FBADeletionResult> FBADeletionResults;
		list<FBAMinimalMediaResult> FBAMinimalMediaResults;
		list<FBAMetaboliteProductionResult> FBAMetaboliteProductionResults;
		list<FBAMinimalReactionsResult> FBAMinimalReactionsResults;
    } FBA;
    
    /* 
    	GapGenerationSolutionReaction object holds data a reaction proposed to be removed from the model
    */
    typedef structure {
    	modelreaction_ref modelreaction_ref;
    	string direction;
    } GapgenerationSolutionReaction;
    
    /* 
    	GapGenerationSolution object holds data on a solution proposed by the gapgeneration command
    */
    typedef structure {
    	gapgensol_id id;
    	float solutionCost;
    	list<modelcompound_ref> biomassSuppplement_refs;
    	list<modelcompound_ref> mediaRemoval_refs;
    	list<modelreaction_ref> additionalKO_refs;
    	bool integrated;
    	bool suboptimal;
    	list<GapgenerationSolutionReaction> gapgenSolutionReactions;
    } GapgenerationSolution;
    
    /* 
    	GapGeneration object holds data on formulation and solutions from gapgen analysis
    	
    	@optional fba_ref totalTimeLimit timePerSolution media_ref referenceMedia_ref gprHypothesis reactionRemovalHypothesis biomassHypothesis mediaHypothesis
    	@searchable ws_subset id totalTimeLimit timePerSolution referenceMedia_ref fbamodel_ref fba_ref reactionRemovalHypothesis gprHypothesis biomassHypothesis mediaHypothesis
    */
    typedef structure {
    	gapgen_id id;
    	fba_ref fba_ref;
    	fbamodel_ref fbamodel_ref;
    	
    	bool mediaHypothesis;
    	bool biomassHypothesis;
    	bool gprHypothesis;
    	bool reactionRemovalHypothesis;
    	
    	media_ref media_ref;
    	media_ref referenceMedia_ref;
    	
    	int timePerSolution;
    	int totalTimeLimit;
    	
    	list<GapgenerationSolution> gapgenSolutions;
    } Gapgeneration;
    
    /* 
    	GapFillingReaction object holds data on a reaction added by gapfilling analysis
    	
    	@optional compartmentIndex round
    */
    typedef structure {
    	int round;
    	reaction_ref reaction_ref;
    	compartment_ref compartment_ref;
    	string direction;
    	int compartmentIndex;
    	list<feature_ref> candidateFeature_refs;
    } GapfillingReaction;
    
    /* 
    	ActivatedReaction object holds data on a reaction activated by gapfilling analysis
    	
    	@optional round
    */
    typedef structure {
    	int round;
    	modelreaction_ref modelreaction_ref;
    } ActivatedReaction;
    
    /*
    	GapFillingSolution object holds data on a solution generated by gapfilling analysis
    	
    	@optional activatedReactions failedReaction_refs
    	@searchable ws_subset id suboptimal integrated solutionCost koRestore_refs biomassRemoval_refs mediaSupplement_refs
    */
    typedef structure {
    	gapfillsol_id id;
    	float solutionCost;
    	
    	list<modelcompound_ref> biomassRemoval_refs;
    	list<modelcompound_ref> mediaSupplement_refs;
    	list<modelreaction_ref> koRestore_refs;
    	bool integrated;
    	bool suboptimal;
    	
    	list<modelreaction_ref> failedReaction_refs;
    	list<ActivatedReaction> activatedReactions;
    	list<GapfillingReaction> gapfillingSolutionReactions;
    } GapfillingSolution;
    
    /* 
    	GapFilling object holds data on the formulations and solutions of a gapfilling analysis
    	
    	@optional simultaneousGapfill totalTimeLimit timePerSolution transporterMultiplier singleTransporterMultiplier biomassTransporterMultiplier noDeltaGMultiplier noStructureMultiplier deltaGMultiplier directionalityMultiplier drainFluxMultiplier reactionActivationBonus allowableCompartment_refs blacklistedReaction_refs targetedreaction_refs guaranteedReaction_refs completeGapfill balancedReactionsOnly reactionAdditionHypothesis gprHypothesis biomassHypothesis mediaHypothesis fba_ref media_ref probanno_ref
    	@searchable ws_subset id totalTimeLimit timePerSolution transporterMultiplier singleTransporterMultiplier biomassTransporterMultiplier noDeltaGMultiplier noStructureMultiplier deltaGMultiplier directionalityMultiplier drainFluxMultiplier reactionActivationBonus allowableCompartment_refs blacklistedReaction_refs targetedreaction_refs guaranteedReaction_refs completeGapfill balancedReactionsOnly reactionAdditionHypothesis gprHypothesis biomassHypothesis fba_ref fbamodel_ref probanno_ref mediaHypothesis
    */
    typedef structure {
    	gapfill_id id;
    	fba_ref fba_ref;
    	media_ref media_ref;
    	fbamodel_ref fbamodel_ref;
    	probanno_ref probanno_ref;
    	
    	bool mediaHypothesis;
    	bool biomassHypothesis;
    	bool gprHypothesis;
    	bool reactionAdditionHypothesis;
    	bool balancedReactionsOnly;
    	bool completeGapfill;
    	bool simultaneousGapfill;
    	
    	list<reaction_ref> guaranteedReaction_refs;
    	list<reaction_ref> targetedreaction_refs;
    	list<reaction_ref> blacklistedReaction_refs;
    	list<compartment_ref> allowableCompartment_refs;
    	
    	float reactionActivationBonus;
    	float drainFluxMultiplier;
    	float directionalityMultiplier;
    	float deltaGMultiplier;
    	float noStructureMultiplier;
    	float noDeltaGMultiplier;
    	float biomassTransporterMultiplier;
    	float singleTransporterMultiplier;
    	float transporterMultiplier;
    	
    	int timePerSolution;
    	int totalTimeLimit;
    	
    	mapping<reaction_ref,float> reactionMultipliers;
    	list<GapfillingSolution> gapfillingSolutions;
    } Gapfilling;
	
    /* 
    	TemplateBiomassComponent object holds data on a compound of biomass in template
    */
	typedef structure {
    	templatebiomasscomponent_id id;
    	string class;
    	compound_ref compound_ref;
    	compartment_ref compartment_ref;
    	
    	string coefficientType;
    	float coefficient;
    	
    	list<compound_ref> linked_compound_refs;
    	list<float> link_coefficients;
    } TemplateBiomassComponent;
    
    /* 
    	TemplateBiomass object holds data on biomass in template
    	
    	@searchable ws_subset id name type other dna rna protein lipid cellwall cofactor energy
    */
	typedef structure {
    	templatebiomass_id id;
    	string name;
    	string type;
    	float other;
    	float dna;
    	float rna;
    	float protein;
    	float lipid;
    	float cellwall;
    	float cofactor;
    	float energy;
    	list<TemplateBiomassComponent> templateBiomassComponents;
    } TemplateBiomass;
    
    /* 
    	TemplateReaction object holds data on reaction in template
    	
    	@optional base_cost forward_penalty reverse_penalty
    */
	typedef structure {
    	templatereaction_id id;
    	reaction_ref reaction_ref;
    	compartment_ref compartment_ref;
    	list<complex_ref> complex_refs;
    	string direction;
    	string type;
    	float base_cost;
    	float forward_penalty;
    	float reverse_penalty;
    } TemplateReaction;
    
    /* 
    	ModelTemplate object holds data on how a model is constructed from an annotation
    	    	
    	@optional name
    	@searchable ws_subset id name modelType domain mapping_ref
    */
	typedef structure {
    	modeltemplate_id id;
    	string name;
    	string modelType;
    	string domain;
    	mapping_ref mapping_ref;
    	Biochemistry_ref biochemistry_ref;
    	
    	list<TemplateReaction> templateReactions;
    	list<TemplateBiomass> templateBiomasses;
    } ModelTemplate;
    
    /* ReactionSensitivityAnalysisCorrectedReaction object
		
		kb_sub_id kbid - KBase ID for reaction knockout corrected reaction
		ws_sub_id model_reaction_wsid - ID of model reaction
		float normalized_required_reaction_count - Normalized count of reactions required for this reaction to function
		list<ws_sub_id> required_reactions - list of reactions required for this reaction to function
		
		@optional
		
	*/
	typedef structure {
		modelreaction_ref modelreaction_ref;
		float normalized_required_reaction_count;
		list<modelreaction_id> required_reactions;
    } ReactionSensitivityAnalysisCorrectedReaction;
	
	/* Object for holding reaction knockout sensitivity reaction data
		
		kb_sub_id kbid - KBase ID for reaction knockout sensitivity reaction
		ws_sub_id model_reaction_wsid - ID of model reaction
		bool delete - indicates if reaction is to be deleted
		bool deleted - indicates if the reaction has been deleted
		float growth_fraction - Fraction of wild-type growth after knockout
		float normalized_activated_reaction_count - Normalized number of activated reactions
		list<ws_sub_id> biomass_compounds  - List of biomass compounds that depend on the reaction
		list<ws_sub_id> new_inactive_rxns - List of new reactions dependant upon reaction KO
		list<ws_sub_id> new_essentials - List of new essential genes with reaction knockout
	
		@optional direction
	*/
	typedef structure {
		string id;
		modelreaction_ref modelreaction_ref;
		float growth_fraction;
		bool delete;
		bool deleted;
		string direction;
		float normalized_activated_reaction_count;
		list<modelcompound_id> biomass_compounds;
		list<modelreaction_id> new_inactive_rxns;
		list<feature_id> new_essentials;
    } ReactionSensitivityAnalysisReaction;
	
	/* Object for holding reaction knockout sensitivity results
	
		kb_id kbid - KBase ID of reaction sensitivity object
		ws_id model_wsid - Workspace reference to associated model
		string type - type of reaction KO sensitivity object
		bool deleted_noncontributing_reactions - boolean indicating if noncontributing reactions were deleted
		bool integrated_deletions_in_model - boolean indicating if deleted reactions were implemented in the model
		list<ReactionSensitivityAnalysisReaction> reactions - list of sensitivity data for tested reactions
		list<ReactionSensitivityAnalysisCorrectedReaction> corrected_reactions - list of reactions dependant upon tested reactions
		
		@searchable ws_subset id fbamodel_ref type deleted_noncontributing_reactions integrated_deletions_in_model
		@optional	
	*/
    typedef structure {
		string id;
		fbamodel_ref fbamodel_ref;
		string type;
		bool deleted_noncontributing_reactions;
		bool integrated_deletions_in_model;
		list<ReactionSensitivityAnalysisReaction> reactions;
		list<ReactionSensitivityAnalysisCorrectedReaction> corrected_reactions;
    } ReactionSensitivityAnalysis;


    /* 
        ETCStep object
    */

    typedef structure {
        list<string> reactions;
    } ETCStep;

    /* 
        ETCPathwayObj object
    */

    typedef structure {
        string electron_acceptor;
        list<ETCStep> steps;
    } ETCPathwayObj;

    /* 
        ElectronTransportChains (ETC) object
    */
    typedef structure {
        list<ETCPathwayObj> pathways;
    } ETC;

    /*
    Object required by the prom_constraints object which defines the computed probabilities for a target gene.  The
    TF regulating this target can be deduced based on the TFtoTGmap object.
    
        string target_gene_ref           - reference to the target gene
        float probTGonGivenTFoff    - PROB(target=ON|TF=OFF)
                                    the probability that the target gene is ON, given that the
                                    transcription factor is not expressed.  Set to null or empty if
                                    this probability has not been calculated yet.
        float probTGonGivenTFon   - PROB(target=ON|TF=ON)
                                    the probability that the transcriptional target is ON, given that the
                                    transcription factor is expressed.    Set to null or empty if
                                    this probability has not been calculated yet.
    */
    typedef structure {
        string target_gene_ref;
        float probTGonGivenTFoff;
        float probTGonGivenTFon;
    } TargetGeneProbabilities;

	/*
    Object required by the prom_constraints object, this maps a transcription factor 
     to a group of regulatory target genes.
    
        string transcriptionFactor_ref                       - reference to the transcription factor
        list<TargetGeneProbabilities> targetGeneProbs        - collection of target genes for the TF
                                                                along with associated joint probabilities for each
                                                                target to be on given that the TF is on or off.
    
    */
    typedef structure {
        string transcriptionFactor_ref;
        list<TargetGeneProbabilities> targetGeneProbs;
    } TFtoTGmap;
    
    /*
    An object that encapsulates the information necessary to apply PROM-based constraints to an FBA model. This
    includes a regulatory network consisting of a set of regulatory interactions (implied by the set of TFtoTGmap
    objects) and interaction probabilities as defined in each TargetGeneProbabilities object.  A link the the annotation
    object is required in order to properly link to an FBA model object.  A reference to the expression_data_collection
    used to compute the interaction probabilities is provided for future reference.
    
        string id                                         - the id of this prom_constraints object in a
                                                                        workspace
        genome_ref									
                                                                        which specfies how TFs and targets are named
        list<TFtoTGmap> transcriptionFactorMaps                                     - the list of TFMaps which specifies both the
                                                                        regulatory network and interaction probabilities
                                                                        between TF and target genes
        expression_series_ref expression_series_ref   - the id of the expresion_data_collection object in
                                                                        the workspace which was used to compute the
                                                                        regulatory interaction probabilities
    
    */
    typedef structure {
        string id;
        genome_ref genome_ref;
        list<TFtoTGmap> transcriptionFactorMaps;
        expression_series_ref expression_series_ref;
		regulome_ref regulome_ref;
    } PromConstraint;
    
    /*
        
    */
    typedef structure {
        string id;
        string description;
        float tp_rate;
        float fb_rate;
        float precision;
        float recall;
        float f_measure;
        float ROC_area;
        mapping<string,int> missclassifications;
    } ClassifierClasses;
    
    /*
        
    */
    typedef structure {
        string id;
        string attribute_type;
        string classifier_type;
        Trainingset_ref trainingset_ref;
        string data;
        string readable;
        int correctly_classified_instances;
        int incorrectly_classified_instances;
        int total_instances;
        float kappa;
        float mean_absolute_error;
        float root_mean_squared_error;
        float relative_absolute_error;
        float relative_squared_error;
        list<ClassifierClasses> classes;
    } Classifier;
    
    /*
        @optional attribute_type source description
    */
    typedef structure {
        string id;
        string description;
        string source;
        string attribute_type;
        list<tuple<genome_ref,string,list<string>>> workspace_training_set; 
		list<tuple<string database,string genome_id,string,list<string>>> external_training_set;
		list<tuple<string,string>> class_data;
    } ClassifierTrainingSet;
    
    /*
    */
    typedef structure {
        string id;
        Classifier_ref classifier_ref;
        list<tuple<genome_ref,string,float>> workspace_genomes; 
		list<tuple<string,string,string,float>> external_genomes;
    } ClassifierResult;
};
