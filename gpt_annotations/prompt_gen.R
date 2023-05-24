## HPO phenotype annotations - code to generate prompts for input into chat GPT ##

# focus on phenotypes that have enrichment results from multiEWCE
all_res <- MultiEWCE::load_example_results()
phenos <- data.frame(Phenotype=unique(all_res$Phenotype))

# we're inputting 3 phenotypes per prompt
batch_size = 3

n_terms <- nrow(phenos)
batches <- split(seq_len(n_terms), 
                 ceiling(seq_along(seq_len(n_terms))/batch_size))

# re-word prompt so that you give instructions first then give phenotypes

# prep prompt 
effects <- "intellectual disability, death, impaired mobility, 
physical malformations, blindness, sensory impairments, 
immunodeficiency, cancer, reduced fertility?"

# define the columns of the output table 
table_columns <- "phenotype, intellectual_disability, death, impaired_mobility, 
physical_malformations, blindness, sensory_impairments, immunodeficiency, cancer, 
reduced_fertility, congenital_onset, justification."


prep_prompt <- function(x){ 
  
  terms <- paste(
    x,
    collapse="; "
  ) 
  
  question <- paste("I need to annotate phenotypes as to whether they typically cause:", 
                   effects, 
                   "Do they have congenital onset?",
                   "You must give one-word yes or no answers.",
                   "Do not consider indirect effects.",
                   "You must provide the output in python code as a data frame called df with columns:",
                   table_columns, 
                   "These are the phenotypes:", 
                   terms)
  question <- gsub("\n", "", question)
  
  return(question)
}

res <- lapply(seq_len(length(batches)), function(i){
  batch_idx <- batches[[i]]
  question <- prep_prompt(x = phenos[batch_idx,])
})

# get data frame of prompts
res2 <- unlist(res)
prompts <- data.table(prompt = res2)
prompts$prompt <- gsub("\n", "", prompts$prompt)

#write.csv(prompts, file="gpt_prompts.csv", quote=T, row.names=F)
