import fire
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(root_dir)

from mymi.processing.dataset.nifti import convert_replan_to_lens_crop

fire.Fire(convert_replan_to_lens_crop)
