from myalexnet_forward_newtf import AlexnetValidation

#with open("ILSVRC2012_validation_ground_truth.txt", "r") as f:
#with open("val.txt", "r") as f:
with open("val_sample.txt", "r") as f:
    correct_classes=f.readlines()

number_of_correct_predictions_top1=0
number_of_correct_predictions_top5=0
with open("alexnet_accuracy_sample.txt", "w") as f:
    #for i in range(999, 1001):
    for i in range(1, 101):
    	if i==2 or i==11 or i==48 or i == 107 or i == 118 or i == 126 or i == 141 or i == 296 or i == 317 or i == 377 or i == 392 or i == 429 or i== 532 or i == 560 or i == 636 or i == 704 or i == 760 or i == 872 or i == 889 or i == 896:
            continue 

    	#result, txt = AlexnetValidation("/home/ershadi1/sparsification_arshia/alexnet/validation_images/"+"ILSVRC2012_val_"+str(i)+".JPEG")
	result, txt = AlexnetValidation("/home/ershadi1/sparsification_arshia/alexnet/imagenet-sample-images/"+"ILSVRC2012_val_"+str(i)+".JPEG") 

	print("\n")
	f.write("\n")

	print("Image: {}".format(i))
	print("\n")
	f.write("Image: {}".format(i))
        f.write("\n")

        for item in txt:
            print(item)
            f.write(item)

	print("\n")
	f.write("\n")
        
        # result will always be from 0 to 999
        print("Result: {}".format(result))
    	f.write("Result: {}".format(result))
	f.write("\n")

        # if using ILSVRC this will be from 1 to 1000, otherwise 0 to 999
        #'''
        print("Correct: {}".format(correct_classes[i-1]))
    	f.write("Correct: {}".format(correct_classes[i-1]))
        f.write("\n") 
        #'''
          
        '''
        print("Correct: {}".format(int(correct_classes[i-1]) - 1))
    	f.write("Correct: {}".format(int(correct_classes[i-1]) - 1))
        f.write("\n") 
        '''           
     
    	if str(result[0]).strip() == correct_classes[i-1].strip():
            number_of_correct_predictions_top1=number_of_correct_predictions_top1+1

	for item in result:
		if str(item).strip() == correct_classes[i-1].strip():
			number_of_correct_predictions_top5=number_of_correct_predictions_top5+1

        print("Number of correct top-1 predictions: {}".format(number_of_correct_predictions_top1))
	print("\n")
        f.write("Number of correct top-1  predictions: {}".format(number_of_correct_predictions_top1))
        f.write("\n")

	
        print("Number of correct top-5 predictions: {}".format(number_of_correct_predictions_top5))
	print("\n")
        f.write("Number of correct top-5  predictions: {}".format(number_of_correct_predictions_top5))
        f.write("\n")

        #if i == 1000:
	if i == 100:
            #print("Accuracy (Top-1): {}".format(str(number_of_correct_predictions/982.0)))
            #f.write("Accuracy (Top-1): {}".format(str(number_of_correct_predictions/982.0)))
            
	    print("Accuracy (Top-1): {}".format(str(number_of_correct_predictions_top1/97.0)))
	    print("\n")
            f.write("Accuracy (Top-1): {}".format(str(number_of_correct_predictions_top1/97.0)))
	    f.write("\n")
    	    print("Accuracy (Top-5): {}".format(str(number_of_correct_predictions_top5/97.0)))
	    print("\n")
            f.write("Accuracy (Top-5): {}".format(str(number_of_correct_predictions_top5/97.0)))
	    f.write("\n")

