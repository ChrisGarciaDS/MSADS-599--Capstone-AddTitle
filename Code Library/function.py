def scale_features(X, scaling_method='minmax'):
    """
    Scale the features in X using Standardization.

    Parameters:
        X (DataFrame): The features DataFrame to be scaled.
        scaling_method (str): The scaling used is Standardization

    Returns:
        DataFrame: The scaled features DataFrame.
    """

    if scaling_method not in ['standard']:
        raise ValueError("Invalid scaling_method. Options 'standard'.")
    else:
        scaler = StandardScaler()

    # Fit and transform the features using the chosen scaler
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X_scaled