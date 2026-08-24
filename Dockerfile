FROM jupyter/pyspark-notebook:latest
USER root
RUN mamba remove -y numexpr bottleneck && \
    mamba clean --all -f -y
RUN pip install --no-cache-dir \
    plotly scikit-learn xgboost lightgbm \
    pandas numexpr>=2.10.2 bottleneck>=1.4.2 \
    sweetviz \
#     streamlit dash
    polars \
    jupyterlab-citation-manager
USER jovyan
