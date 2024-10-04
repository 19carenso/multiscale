import os
import glob
import sys
import yaml

from tempest import casestudy
from tempest import grid
from tempest import handler
from tempest import joint_distrib
from tempest import storm_tracker

settings_path = "settings/arpege_summer_30d.yaml"

workdir=os.getcwd()
print(workdir)
sys.path.append(workdir)

# Instantiate CaseStudy by passing the settings. 
# Should also create appropriate directories
hdlr = handler.Handler(settings_path)
overwrite = False
cs = casestudy.CaseStudy(hdlr, overwrite = overwrite ,verbose = True)
gr = grid.Grid(cs, fast = True, overwrite= overwrite, verbose_steps = False, verbose = False)

if __name__ == '__main__':
    # 1st batch 
    gr.compute_funcs_for_var_id("Prec", overwrite_var_id=True)
    gr.compute_funcs_for_var_id("MCS_label", overwrite_var_id=True)
    gr.compute_funcs_for_var_id("MCS_Feng", overwrite_var_id=True)
    
    print("Storm tracking clouds")
    st = storm_tracker.StormTracker(gr, label_var_id = "MCS_label", overwrite_storms = True, overwrite = False)
    print("Storm tracking mcs")
    st = storm_tracker.StormTracker(gr, label_var_id = "MCS_Feng", overwrite_storms = True, overwrite = False)

    # # 2nd batch
    gr.compute_funcs_for_var_id("vDCS", overwrite_var_id=True)
    gr.compute_funcs_for_var_id("MCS_cond_Prec_15", overwrite_var_id = True)
    gr.compute_funcs_for_var_id("vDCS_cond_Prec_15")
    gr.compute_funcs_for_var_id("clouds_cond_Prec_15")
    st = storm_tracker.StormTracker(gr, label_var_id = "vDCS", overwrite_storms = True, overwrite = False)

    cloud_types = ["clouds_cond_prec_25", "vdcs_cond_prec_25", "mcs_cond_prec_25"]
    for cloud_type in cloud_types:
        gr.build_cloud_intersect(cloud_type, coverage_threshold=0.5)