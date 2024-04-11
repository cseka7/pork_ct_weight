import os

threshold=0.5

bin_width=20
bin_min=-200
bin_max=200

bin_width_body=50
bin_min_body=-200
bin_max_body=2000

path_prefix_data= 'data'
path_prefix_results= 'results'
os.makedirs(path_prefix_results, exist_ok=True)
manually_segmented_path=os.path.join(path_prefix_data, 'manually_labels')
dissected_path=os.path.join(path_prefix_data, 'dissected')
leg_features_path=os.path.join(path_prefix_data, 'leg_training_features-%d-%.2f.csv' % (bin_width, threshold))
loin_features_path=os.path.join(path_prefix_data, 'loin_training_features-%d-%.2f.csv' % (bin_width, threshold))
belly_features_path=os.path.join(path_prefix_data, 'belly_training_features-%d-%.2f.csv' % (bin_width, threshold))
groin_features_path=os.path.join(path_prefix_data, 'groin_training_features-%d-%.2f.csv' % (bin_width, threshold))
shoulder_features_path=os.path.join(path_prefix_data, 'shoulder_training_features-%d-%.2f.csv' % (bin_width, threshold))
body_features_path=os.path.join(path_prefix_data, 'body_training_features-%d-%.2f.csv' % (bin_width_body, threshold))
xls_path= os.path.join(path_prefix_data, 'pigweb.xlsx')

save_registered_images=True

output_path=os.path.join(path_prefix_data, 'training')
tmp_path=os.path.join(path_prefix_data, 'tmp')
os.makedirs(output_path, exist_ok=True)
os.makedirs(tmp_path, exist_ok=True)

files_for_lmp_path=os.path.join(path_prefix_data, "files_for_lmp")
lmp_features_path=os.path.join(path_prefix_data, 'lmp_features-%d-%d-%d.csv' % (bin_min, bin_max, bin_width))

threads = 12
elastix_params= {'FixedImageDimension': 3,
         'MovingImageDimension': 3,
         'WriteResultImage': "true",
         'ResultImagePixelType': "double",
         'FixedInternalImagePixelType': "float",
         'MovingInternalImagePixelType': "float",
         'UseDirectionCosines': "true",
         'Registration': "MultiResolutionRegistration",
         'FixedImagePyramid': "FixedRecursiveImagePyramid",
         'MovingImagePyramid': "MovingRecursiveImagePyramid",
         'HowToCombineTransforms': "Compose",
         'DefaultPixelValue': -1024,
         'Interpolator': "BSplineInterpolator",
         'BSplineInterpolationOrder': "1",
         'ResampleInterpolator': "FinalBSplineInterpolator",
         'FinalBSplineInterpolationOrder': 3,
         'Resampler': "DefaultResampler",
         'Metric': "AdvancedMattesMutualInformation",
         'NumberOfHistogramBins': 32,
         'ImageSampler': "RandomCoordinate",
         'NumberOfSpatialSamples': 4048,
         'NewSamplesEveryIteration': "true",
         'NumberOfResolutions': 4,
         'Transform': "BSplineTransform",
         'Optimizer': "AdaptiveStochasticGradientDescent",
         'MaximumNumberOfIterations': 200,
         'FinalGridSpacingInVoxels': [10, 10, 10],
         'ResultImageFormat': "nii.gz",
         'CheckNumberOfSamples': "false",
         "RandomSeed": 5}


