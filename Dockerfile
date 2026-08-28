FROM jupyter/pyspark-notebook:latest
USER root
RUN mamba remove -y numexpr bottleneck && \
    mamba clean --all -f -y
RUN pip install --no-cache-dir \
    polars pandas "numexpr>=2.10.2" "bottleneck>=1.4.2" \
    plotly \
    scikit-learn xgboost lightgbm tensorflow \
    sweetviz \
#     streamlit dash
    jupyterlab-citation-manager
USER jovyan
