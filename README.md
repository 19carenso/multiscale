0) adapt paths in settings/*.yaml to your own architecture, especially your /data/
1) launch scripts/main.py for every yaml file in settings (should take 2 to 3 days), populates /data/
2) up to 1 Tbytes will be written (not really optimized but could no go much lower imo)
4) plots are produced in analysis by either notebooks or python code and save in output (hopefully)
5) launching code in analysis/ will populate /data/ with underlying plot (light)
   
I should add mine in some way somwehere so that you don't have to launch the main.py, but anyway if you need to play around
   with the data you will still have to launch the main !
