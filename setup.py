import setuptools

setuptools.setup(
    name="lookup",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=["lookup"],
    classifiers=[],
    python_requires=">=3.6",
    # install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        
    # ],
    
    entry_points={"console_scripts": ["lookup = lookup.cli:main"]},

)
