import setuptools

setuptools.setup(
    name="alerts",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=["alerts"],
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        
        "appdirs == 1.4.4",
        "fire == 0.4.0",
        "slack-sdk==3.19.2",
        "loguru == 0.6.0",
    ],
    
    entry_points={"console_scripts": ["tiny_queue = tiny_queue.cli:main"]},

)
