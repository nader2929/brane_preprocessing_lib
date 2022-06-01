# Preprocesing
This library is to be used for preprocessing data and training classifiers. 
## Functions

---

`drop_columns` : Take a CSV file and drop the specified columns such that a new file is created without those columns at a similarily named CSV file, the filename will be the same plus `_red` (for reduced) before eh extension. E.g. Drop "['Name', 'Ticket', 'Fare', 'Cabin']" from train.csv and save the result into train_red.csv.

> Input

- `columns_to_drop : string` : A string in the format of a list of string that is formatted is as "['value1', 'value2', 'value3', 'value4', 'value5', ...]" indicating the columns to drop from the dataset provided.
- `data_path : string` : The path in the Brane environment to find the data to use.

> Output

- `resultOutput : string` : A string explaing where the file has been saved.

---

`analyse_column` : Get the basic categorical stats on a column in a CSV file and write the stats to a new CSV file. Function assumes that the column is a categorical column. The file that the stats will be saved to will be called `/data/COLUMN_analysed.csv`. The input must be a CSV file.

> Input

- `column : string` : The column in the dataset to analyse. Is a string value. 
- `printMessages : boolean`: Whether to print messages about the steps being taken in the execution of the function. (Currently disabled).
- `data_path : string` : The path in the Brane environment to find the data to use.

> Output

- `resultOutput` : A string explaing where the file has been saved. 

---

`analyse_column_with_filter` : Do the same categorical analysis as the `analyse_column` function except additionally splitting the data on some filter column and analyse the difference of the main column by splitting on that filter column. The file that the stats will be saved to will be called `/data/COLUMN_analysed_with_filter.csv`. The input must be a CSV file. 

> Input

- `column : string` : The column in the dataset to analyse. Is a string value. 
- `fitler_column : string`: The column by which to split the data and examine the impact it has on the `column`.
- `printMessages : boolean`: Whether to print messages about the steps being taken in the execution of the function. (Currently disabled).
- `data_path : string` : The path in the Brane environment to find the data to use.

> Output

- `resultOutput : string` : A string explaing where the file has been saved. 

---

`replace_string_values` : Take a CSV file and replace the specified string columns such that they are replaced by integers. E.g. The column "sex" will replace the values "Male" and "Female" with 1 and 2.

> Input

- `string_columns : string` : A string in the format of a list of string that is formatted is as "['value1', 'value2', 'value3', 'value4', 'value5', ...]" indicating the columns to replace the string values of.
- `data_path : string` : The path in the Brane environment to find the data to use.

> Output

- `resultOutput : string` : A string explaing where the file has been saved.

---

`train_and_test_classifier` : Train a classifier to predict the value of a target column based on the features in the provided dataset. The model will then be pickled and saved to a file at `/data/MODEL_TYPE_trained.pkl`.

> Input

- `target_column : string` : The target feature for which to train the classifer to predict.

- `test_size : real` : The amount of the training data to reserve to test the accuracy of the classifier.

- `model_type : string` : The type of the classifier to train. There are 5 options: "dtree" (Decision Tree), "knn" (K Nearest Neighbour), "rf" (Random Forest), "mlp" (Multilayer Perceptron), "ada" (AdaBoost Classifier)

- `exclude_first_column : boolean` : Whether or not to exclude the first column from the training process.

- `replace_strings : boolean` : Whether or not to replace the strings in the data columns before training the model.

- `data_path : string` : The path in the Brane environment to find the data to use to train the model.

> Output

- `resultOutput : string` : A string explaing where the model has been saved.

---

`load_classifier_and_predict` : Load a model from a pickle file and then predict the target variable of the model for the data provided. The predictions will be saved to a file `/data/model_predictions.csv` that will have a column as an index and a column for the predicted value.

> Input

- `model_path : string` : The path that the pickled model is saved in.

- `predict_data_path : string` : The path to the data that the classifer will predict the target variable for.

- `prediction_column_name : string` : The name to give the CSV column of the predicted variable.

- `replace_strings : boolean` : Replace the strings in the data as integers that represent their categorical value.

- `use_first_column_as_index : boolean` : Use the first column as the index for the predictions in the output CSV file. If `false` then just use an auto-incrementing number starting from 1.


> Output

- `resultOutput : string` : A string explaing where the file with the predictions of the model has been saved.
