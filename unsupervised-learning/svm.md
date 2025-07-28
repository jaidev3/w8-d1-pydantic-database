## 1. What is a Support Vector Machine (SVM)?  
A **Support Vector Machine (SVM)** is a supervised machine learning algorithm primarily used for classification (and sometimes regression) tasks. Its main objective is to find the best possible boundary (hyperplane) that separates classes of data with the maximum margin, effectively distinguishing between different categories of input data.

## 2. Define the following terms in the context of SVM:  
- **Hyperplane:** A hyperplane is a decision boundary that divides the feature space into different classes. For a two-dimensional space, it's a line; for higher dimensions, it becomes a plane or a higher-dimensional analog.
- **Support Vectors:** These are the data points that are closest to the hyperplane. They are pivotal in defining the position and orientation of the hyperplane, as the margin is measured based on these points.
- **Margin:** The margin is the distance between the hyperplane and the nearest support vectors from each class. A larger margin is generally preferred, indicating a clearer separation between classes.

## 3. Why does SVM aim to maximize the margin? How does it affect model generalization?  
SVM seeks to maximize the margin because a larger margin between the classes typically leads to better generalization ability. Maximizing the margin reduces the risk of overfitting and enables the model to perform well on unseen data by ensuring that the decision boundary is robust and less sensitive to slight variations in the data.

## 4. What is the difference between a hard margin and a soft margin in SVM?  
- **Hard Margin:** Assumes all data is linearly separable without error. No misclassification is allowed, which can be too strict for real-world, noisy data.
- **Soft Margin:** Allows for some misclassification or violations of the margin. It introduces a penalty for misclassified points, providing flexibility to handle overlapping or noisy datasets.

## 5. Explain the concept of the kernel trick. Why is it useful in SVM?  
The **kernel trick** is a method that allows SVMs to operate in a high-dimensional (possibly infinite-dimensional) feature space without explicitly transforming the data. It computes the inner products in this space efficiently using kernel functions (e.g., RBF, polynomial). This is useful for solving problems where data is not linearly separable in the original feature space.

## 6. Differentiate between the following kernel types:

| Kernel Type | Description | Example Use |
| ----------- | ----------- | ----------- |
| Linear      | No transformation; fits a linear hyperplane in original space. | Text classification, where features are already linearly separable. |
| Polynomial | Maps input to a higher-dimensional space using polynomial functions. Captures interaction of features up to a certain degree. | Image processing, tasks with polynomial relationships between variables. |
| RBF (Radial Basis Function) | Maps inputs to an infinite-dimensional space; handles complex, non-linear boundaries. | Bioinformatics, where class boundaries are highly non-linear. |

## 7. What do the hyperparameters C and gamma control in an SVM model?
- **C (Regularization Parameter):** Controls the trade-off between maximizing the margin and minimizing classification errors. A low C increases margin but allows more misclassifications; a high C tries to classify all points correctly but may lead to overfitting.
- **Gamma:** Controls the influence of single training examples in RBF/poly kernels. Low gamma means points far from the hyperplane are considered; high gamma means only those close to the hyperplane influence the model.

## 8. Give two real-world use cases of SVM and briefly explain how SVM is useful in those scenarios.
- **Email Spam Detection:** SVMs can classify emails as spam or not-spam by learning from labeled examples of both, efficiently handling large feature sets like words and phrases.
- **Handwritten Digit Recognition:** SVMs can classify images of handwritten digits (e.g., MNIST dataset) by finding optimal boundaries in high-dimensional pixel spaces, even when digits are not linearly separable.

## 9. When would you prefer to use:
- **Linear kernel:** When the data is (almost) linearly separable or the number of features is much higher than the number of data points (e.g., text data).
- **RBF kernel:** When the data shows complex, non-linear relationships and cannot be separated by a straight line or hyperplane in the original feature space.

## 10. List two advantages and two disadvantages of using SVM.

| Advantages                        | Disadvantages      |
| ---------------------------------- | ----------------- |
| Effective in high-dimensional spaces; robust to overfitting (with proper regularization). | Not well-suited for very large datasets due to high computational cost. |
| Can model non-linear boundaries using kernels. | Performance drops if there’s significant class overlap or data noise. |

Sources
