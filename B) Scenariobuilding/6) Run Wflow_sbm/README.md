# 6) Run Wflow_sbm

Wflow_sbm is run in the programming language Julia, specified by https://deltares.github.io/Wflow.jl/stable/user_guide/step4_running/. First specify the path to the toml file (toml_path = ...), where all the required information of the model is given. Next, open Wflow by the code <I>Using Wflow</I>. Lastly, the Wflow_sbm model is run by <I>Wflow.run(toml_path)</I>.

## Postprocess Wflow_sbm output
The Wflow_sbm output requires postprocessing before it can be used in D-HYDRO. The postprocessing consists of two steps, which are executed in the corresponding Notebook. The first step is renaming the lateral output. Wflow_sbm gives each lateral a number, but we want to use the lateral names in D-HYDRO. The second step consists of dividing the lateral output over multiple D-HYDRO laterals. Wflow_sbm contains less laterals than D-HYDRO, because of the resolution. The lateral output of Wflow_sbm is equally spread over the corresponding D-HYDRO laterals within the subsubcatchment. This improves the stability of the D-HYDRO model. 
