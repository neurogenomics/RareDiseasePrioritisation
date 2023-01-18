README
================
Momoko Otani, Brian M. Schilder, Nathan G. Skene
<h4> ¶ README updated: <i>Jan-18-2023</i> ¶ </h4>

# Install packages

``` r
if(!require("remotes")) install.packages("remotes")
```

    ## Loading required package: remotes

``` r
if(!require("MultiEWCE")) remotes::install_github("neurogenomics/MutltiEWCE")
```

    ## Loading required package: MultiEWCE

    ## Registered S3 method overwritten by 'ggnetwork':
    ##   method         from  
    ##   fortify.igraph ggtree

# Prioritise targets

## Gather data

``` r
results <- MultiEWCE::load_example_results()
ctd <- MultiEWCE::load_example_ctd()
```

## Run filtering/sorting procedure

``` r
top_targets <- MultiEWCE::prioritise_targets(results = results,
                                             ctd = ctd)
```

    ## Prioritising gene targets.

    ## Importing existing file: /Users/schilder/Library/Caches/org.R-project.R/R/HPOExplorer/data/phenotype_to_genes.txt

    ## Prioritised targets: 
    ##  - 424,039 results 
    ##  - 5,507 phenotypes 
    ##  - 77 cell types 
    ##  - 0 associated diseases 
    ##  - 0 genes

    ## Filtering @ q-value <= 0.05

    ## Prioritised targets: 
    ##  - 7,545 results 
    ##  - 2,527 phenotypes 
    ##  - 77 cell types 
    ##  - 0 associated diseases 
    ##  - 0 genes

    ## Filtering @ fold-change >= 1

    ## Prioritised targets: 
    ##  - 7,545 results 
    ##  - 2,527 phenotypes 
    ##  - 77 cell types 
    ##  - 0 associated diseases 
    ##  - 0 genes

    ## Annotating phenos with Tiers.

    ## Prioritised targets: 
    ##  - 106 results 
    ##  - 11 phenotypes 
    ##  - 36 cell types 
    ##  - 0 associated diseases 
    ##  - 0 genes

    ## Importing existing file: /Users/schilder/Library/Caches/org.R-project.R/R/HPOExplorer/data/phenotype.hpoa

    ## Annotating phenos with Onset.

    ## Importing existing file: /Users/schilder/Library/Caches/org.R-project.R/R/HPOExplorer/data/phenotype.hpoa

    ## Prioritised targets: 
    ##  - 523 results 
    ##  - 11 phenotypes 
    ##  - 36 cell types 
    ##  - 42 associated diseases 
    ##  - 0 genes

    ## 20 / 36 of cell types kept.

    ## Prioritised targets: 
    ##  - 342 results 
    ##  - 11 phenotypes 
    ##  - 20 cell types 
    ##  - 42 associated diseases 
    ##  - 0 genes

    ## Filtering by gene size.

    ## Converting phenos to GRanges.

    ## Loading required namespace: EnsDb.Hsapiens.v75

    ## Gathering gene metadata

    ## 120 / 2,213 genes kept.

    ## Filtering by specificity_quantile.

    ## Prioritised targets: 
    ##  - 389 results 
    ##  - 11 phenotypes 
    ##  - 0 cell types 
    ##  - 0 associated diseases 
    ##  - 120 genes

    ## Prioritised targets: 
    ##  - 453 results 
    ##  - 9 phenotypes 
    ##  - 17 cell types 
    ##  - 39 associated diseases 
    ##  - 27 genes

    ## Sorting rows.

    ## Finding top 3 gene targets per: HPO_ID, CellType

    ## Prioritised targets: 
    ##  - 96 results 
    ##  - 9 phenotypes 
    ##  - 17 cell types 
    ##  - 17 associated diseases 
    ##  - 22 genes

# Session info

<details>

``` r
utils::sessionInfo()
```

    ## R version 4.2.1 (2022-06-23)
    ## Platform: x86_64-apple-darwin17.0 (64-bit)
    ## Running under: macOS Big Sur ... 10.16
    ## 
    ## Matrix products: default
    ## BLAS:   /Library/Frameworks/R.framework/Versions/4.2/Resources/lib/libRblas.0.dylib
    ## LAPACK: /Library/Frameworks/R.framework/Versions/4.2/Resources/lib/libRlapack.dylib
    ## 
    ## locale:
    ## [1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8
    ## 
    ## attached base packages:
    ## [1] stats     graphics  grDevices utils     datasets  methods   base     
    ## 
    ## other attached packages:
    ## [1] MultiEWCE_0.1.2 remotes_2.4.2  
    ## 
    ## loaded via a namespace (and not attached):
    ##   [1] backports_1.4.1               AnnotationHub_3.6.0          
    ##   [3] BiocFileCache_2.6.0           plyr_1.8.8                   
    ##   [5] lazyeval_0.2.2                orthogene_1.4.1              
    ##   [7] ewceData_1.6.0                BiocParallel_1.32.5          
    ##   [9] GenomeInfoDb_1.34.6           ggnetwork_0.5.10             
    ##  [11] ggplot2_3.4.0                 digest_0.6.31                
    ##  [13] ensembldb_2.22.0              yulab.utils_0.0.6            
    ##  [15] htmltools_0.5.4               RNOmni_1.0.1                 
    ##  [17] fansi_1.0.3                   magrittr_2.0.3               
    ##  [19] memoise_2.0.1                 ontologyPlot_1.6             
    ##  [21] limma_3.54.0                  Biostrings_2.66.0            
    ##  [23] matrixStats_0.63.0            R.utils_2.12.2               
    ##  [25] prettyunits_1.1.1             colorspace_2.0-3             
    ##  [27] blob_1.2.3                    rappdirs_0.3.3               
    ##  [29] xfun_0.36                     dplyr_1.0.10                 
    ##  [31] crayon_1.5.2                  RCurl_1.98-1.9               
    ##  [33] jsonlite_1.8.4                graph_1.76.0                 
    ##  [35] ape_5.6-2                     glue_1.6.2                   
    ##  [37] gtable_0.3.1                  zlibbioc_1.44.0              
    ##  [39] XVector_0.38.0                HGNChelper_0.8.1             
    ##  [41] DelayedArray_0.24.0           car_3.1-1                    
    ##  [43] Rgraphviz_2.42.0              SingleCellExperiment_1.20.0  
    ##  [45] BiocGenerics_0.44.0           abind_1.4-5                  
    ##  [47] scales_1.2.1                  DBI_1.1.3                    
    ##  [49] rstatix_0.7.1                 Rcpp_1.0.9                   
    ##  [51] progress_1.2.2                viridisLite_0.4.1            
    ##  [53] xtable_1.8-4                  gridGraphics_0.5-1           
    ##  [55] tidytree_0.4.2                bit_4.0.5                    
    ##  [57] stats4_4.2.1                  htmlwidgets_1.6.1            
    ##  [59] httr_1.4.4                    ontologyIndex_2.10           
    ##  [61] HPOExplorer_0.99.2            ellipsis_0.3.2               
    ##  [63] XML_3.99-0.13                 pkgconfig_2.0.3              
    ##  [65] R.methodsS3_1.8.2             dbplyr_2.3.0                 
    ##  [67] utf8_1.2.2                    ggplotify_0.1.0              
    ##  [69] tidyselect_1.2.0              rlang_1.0.6                  
    ##  [71] reshape2_1.4.4                later_1.3.0                  
    ##  [73] AnnotationDbi_1.60.0          munsell_0.5.0                
    ##  [75] BiocVersion_3.16.0            tools_4.2.1                  
    ##  [77] cachem_1.0.6                  cli_3.6.0                    
    ##  [79] generics_0.1.3                RSQLite_2.2.20               
    ##  [81] ExperimentHub_2.6.0           statnet.common_4.7.0         
    ##  [83] broom_1.0.2                   evaluate_0.20                
    ##  [85] stringr_1.5.0                 fastmap_1.1.0                
    ##  [87] EnsDb.Hsapiens.v75_2.99.0     yaml_2.3.6                   
    ##  [89] ggtree_3.6.2                  babelgene_22.9               
    ##  [91] knitr_1.41                    bit64_4.0.5                  
    ##  [93] purrr_1.0.1                   AnnotationFilter_1.22.0      
    ##  [95] KEGGREST_1.38.0               gprofiler2_0.2.1             
    ##  [97] nlme_3.1-161                  mime_0.12                    
    ##  [99] R.oo_1.25.0                   grr_0.9.5                    
    ## [101] aplot_0.1.9                   xml2_1.3.3                   
    ## [103] biomaRt_2.54.0                compiler_4.2.1               
    ## [105] rstudioapi_0.14               plotly_4.10.1                
    ## [107] filelock_1.0.2                curl_5.0.0                   
    ## [109] png_0.1-8                     interactiveDisplayBase_1.36.0
    ## [111] ggsignif_0.6.4                treeio_1.22.0                
    ## [113] paintmap_1.0                  tibble_3.1.8                 
    ## [115] EWCE_1.6.0                    homologene_1.4.68.19.3.27    
    ## [117] stringi_1.7.12                GenomicFeatures_1.50.3       
    ## [119] lattice_0.20-45               ProtGenerics_1.30.0          
    ## [121] Matrix_1.5-3                  vctrs_0.5.1                  
    ## [123] pillar_1.8.1                  lifecycle_1.0.3              
    ## [125] BiocManager_1.30.19           data.table_1.14.6            
    ## [127] bitops_1.0-7                  rtracklayer_1.58.0           
    ## [129] httpuv_1.6.8                  patchwork_1.1.2              
    ## [131] GenomicRanges_1.50.2          BiocIO_1.8.0                 
    ## [133] R6_2.5.1                      promises_1.2.0.1             
    ## [135] network_1.18.0                IRanges_2.32.0               
    ## [137] codetools_0.2-18              assertthat_0.2.1             
    ## [139] SummarizedExperiment_1.28.0   rjson_0.2.21                 
    ## [141] GenomicAlignments_1.34.0      Rsamtools_2.14.0             
    ## [143] S4Vectors_0.36.1              GenomeInfoDbData_1.2.9       
    ## [145] hms_1.1.2                     parallel_4.2.1               
    ## [147] grid_4.2.1                    ggfun_0.0.9                  
    ## [149] tidyr_1.2.1                   coda_0.19-4                  
    ## [151] rmarkdown_2.19                MatrixGenerics_1.10.0        
    ## [153] carData_3.0-5                 ggpubr_0.5.0                 
    ## [155] piggyback_0.1.4               Biobase_2.58.0               
    ## [157] shiny_1.7.4                   restfulr_0.0.15

</details>
<hr>
