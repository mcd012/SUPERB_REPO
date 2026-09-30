from sklearn.preprocessing import PolynomialFeatures


class MyRegression:
    def __init__(
        self,
        degree
    ):
        self._poly = PolynomialFeatures(
            degree=degree


    def 
X = np.array([[1], [2], [3]])
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
print(X_poly)