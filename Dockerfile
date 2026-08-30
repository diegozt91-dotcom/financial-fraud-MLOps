FROM jupyter/pyspark-notebook:latest
USER root
RUN mamba remove -y numexpr bottleneck && \
    mamba clean --all -f -y
RUN pip install --no-cache-dir \
    polars pandas "numexpr>=2.10.2" "bottleneck>=1.4.2" \
    plotly dash dash-bootstrap-components \
    scikit-learn xgboost lightgbm tensorflow \
    sweetviz \
    jupyterlab-citation-manager
RUN jupyter labextension develop --overwrite . || jupyter lab build
USER jovyan
