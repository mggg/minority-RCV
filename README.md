# RCV and minority representation

This Python code base accompanies the paper [Ranked Choice Voting and Minority Representation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3778021) by Benade, Buck, Gold, Duchin and Weighill. The STV simulations for each case study are available as standalone `.py` files and print their output in a format suitable for inclusion into `template_table.tex`. To run the simulations for a different jurisdiction or hypothetical scenario, simply duplicate one of these files and adjust the parameters at the top.

<<<<<<< HEAD
The repo also contains the Census and election data used in the case studies (Terrebonne Parish LA, Cincinnati OH, Jones County NC and Pasadena TX) in the paper.
=======
To use this code base, copy and adapt `run_all_models_and_print_output.py` by adjusting the parameters to suit the particular election or jurisdiction you want to study. Then run the new file to cycle through all four models and all five scenarios. The results will be printed as rows of values separated by &s for easy input into LaTeX tables. The files `run_all_models_with_sys_args.py`, `runcityargs.sh`, and `set_parameters.py` are meant to be used for running the models in parallel on a remote server, and can be ignored. 

The `template_table.tex` file contains a basic template for recording these results, including a very brief overview of the models and a blank table with headers.

The repo also contains the Census and election data used in the case studies (Terrebonne Parish LA, Cincinnati OH, Jones County NC and Pasadena TX) in the upcoming report. 
>>>>>>> d2b65fe665ff3e5b12ffdcabf3166a1dc193cebd
