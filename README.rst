Case study of estimating the weights of pork from the CT images of pig
====

About
----

Contents
----

Jupyter notebooks
****

1. ```000_extract_training_features.ipynb``` - segmentation by registration and feature extraction.
2. ```001_training.ipynb``` - feature subset and regressor parameter selection.
3. ```002_analysis.ipynb``` - the statistical analysis of the results, reproducing all the tables in the paper.
4. ```003_orchestration.ipynb``` - executes all notebooks

Other files
****

.. 1. ```config.py``` - high level configuration parameters.
.. 2. ```requirements.txt``` - package requirements.
.. 3. ```results.csv``` - raw results of the regression analysis with feature selection.
.. 4. ```results.pickle``` - raw results of the regression analysis with feature selection in pickle format.
.. 5. ```results.csv``` - raw results of the regression analysis without feature selection.
.. 6. ```results.pickle``` - raw results of the regression analysis without feature selection in pickle format.
.. 7. ```thigh_r2.tex``` - collected r^2 results of the thigh in tex (typesetting language) format.
.. 8. ```brest_r2.tex``` - collected r^2 results of the brest in tex (typesetting language) format.
.. 9. ```thigh_rmse.tex``` - collected rmse results of the thigh in tex (typesetting language) format.
.. 10. ```brest_rmse.tex``` - collected rmse results of the thigh in tex (typesetting language) format.
.. 11. ```pork_dissected_data.xlsx``` - results of the dissection study.

Reproducing the results of the paper
----

Installation
****

Clone the ```maweight``` Python package (https://github.com/cseka7/maweight):

.. code-block:: bash

    > git clone https://github.com/cseka7/maweight.git


Navigate into the root directory of the ```maweight``` repository and issue

.. code-block:: bash

    > pip install .

Clone this package (pork_ct_weights):

.. code-block:: bash

    > git clone https://github.com/cseka7/pork_ct_weights.git


Navigate into the root directory of this package, and issue

.. code-block:: bash

    > pip install -r requirements.txt

Download the raw data
****

Download the CT images corresponding to the dissection study and the manual annotations from the link https://drive.google.com/file/d/1OSuIPioxqATuH4Q3VsUCBcCPUWHNsl1y/view?usp=sharing and extract its contents to the ```data``` directory.

Update the paths
****

Update the paths in the file ```config.py``` to match the environment the code is running in.

Execute the notebooks
****

Start a jupyter server in the active environment by issuing

.. code-block:: bash

    > jupyter notebook

And run the notebook ```003_orchestration.ipynb``` to carry out all steps of the analysis.

Note that due to the large number of CT images and registered masks, the execution requires about 40Gb free space on the disk.
