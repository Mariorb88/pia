import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def execute_notebook():
    # Load the notebook
    with open('tarea5.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {})
    
    # Create a namespace to store executed variables and functions
    namespace = {}
    
    # Extract all cells and execute them in a common namespace
    for cell in nb.cells:
        if cell['cell_type'] == 'code':
            try:
                exec(cell['source'], namespace)
            except Exception as e:
                print(f"Error executing cell: {cell['source']}")
                raise
    
    return namespace

def test_notebook_execution():
    
    import matplotlib.pyplot as plt
    plt.show = lambda: None  # Mock plt.show
    
    notebook_namespace = execute_notebook()
    
    checks = [ # List of variables/functions to check
        'matrix_first_100_labels',
        'X_train_flat',
        'X_test_flat',
        'plot_image',
        'y_train_onehot',
        'y_test_onehot',
        'X_train_norm',
        'X_train_standardized',
        
        'X_train_noisy',
        'binarize_image',
        'X_train_binarized',
        'X_train_noisy_binarized',
        'shift_image',
        'X_train_shifted_right_10',
        'find_limits',
        'crop_image_limits',
        'X_train_shifted',
        'X_train_augmented',
        
        
        
    ]

    for item in checks:
        assert item in notebook_namespace, f"{item} not found in notebook"
    
    # Assign all variables to the namespace
    globals().update(notebook_namespace)
    
    
    assert matrix_first_100_labels.shape == (10, 10)
    assert matrix_first_100_labels[0, 0] == 5
    assert matrix_first_100_labels[1, 0] == 3
    assert matrix_first_100_labels[9, 9] == 1

    assert X_train_flat.shape == (60000, 28*28)
    assert X_test_flat.shape == (10000, 28*28)
    
    plot_image(X_train_flat[0])
    
    assert y_train_onehot.shape == (60000, 10)
    assert y_test_onehot.shape == (10000, 10)
    
    assert y_train_onehot[0, 5] == 1
    assert y_train_onehot[1, 0] == 1
    assert y_train_onehot[99, 1] == 1
    
    assert y_train_onehot[range(5), y_train[:5]].all()
    assert np.all(y_train_onehot.sum(axis=1) == 1)

    assert X_train_norm.shape == (60000, 28, 28)
    assert X_train_norm.min() == 0
    assert X_train_norm.max() == 1
    
    assert np.isclose(pixel_norm_mean, 0.130660)
    assert np.isclose(pixel_norm_std, 0.308107)
    
        
    assert np.isclose(X_train_standardized.mean(), 0)
    assert np.isclose(X_train_standardized.std(), 1)
    
    assert np.isclose(X_train_norm.mean(), 0.130660)
    assert np.isclose(X_train_norm.std(), 0.308107)
    
    assert X_train_noisy.shape == (60000, 28, 28)
    assert X_train_noisy.min() >= 0
    assert X_train_noisy.max() <= 255
    
    assert binarize_image(X_train_noisy[0]).shape == (28, 28)
    assert binarize_image(X_train_noisy[0]).min() == 0
    assert binarize_image(X_train_noisy[0]).max() == 1
    
    assert X_train_binarized.shape == (60000, 28, 28)
    assert X_train_binarized.min() == 0
    assert X_train_binarized.max() == 1
    
    assert X_train_noisy_binarized.shape == (60000, 28, 28)
    assert X_train_noisy_binarized.min() == 0
    assert X_train_noisy_binarized.max() == 1
    
    assert shift_image(X_train[0], 10, 0).shape == (28, 28)
    
    assert find_limits(X_train[0]) == (5, 24, 4, 23)
    
    assert crop_image_limits(X_train[0]).shape == (20, 20)

    assert X_train_augmented.shape == (300000, 28, 28)