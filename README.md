# alexnet
- implementation and evaluation of alexnet 

- myalexnet_forward_newtf.py and bvlc_alexnet.npy pretrained and implemented by http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/

- myalexnet_forward_newtf_arshia.py and myalexnet_forward_newtf_wrapper_arshia.py:

  - I have modified the implementation to be able to run with any number of validation images that user wants and compare results against     a validation ground truth text file with the correct labels of the  validation images that user provides (val_sample.txt in this case       which happens to be a sample of 100 images of imagenet)

  - this is because there is no widely used and easy to use tf slim implementation and evaluation of alexnet as of now, so my script that     wraps this current implementation is a good way to use a pretrained alexnet model and evaluate and report its top-1 and top-5 accuracy     for any given number of images 
