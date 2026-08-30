import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.io as pio

## Cargamos las figuras guardadas en plotly
fig_demographic = pio.read_json("figuras/dem_mcc/demographic.json")
fig_mcc_log2RF = pio.read_json("figuras/dem_mcc/mcc_log2RF.json")

fig_transactions_evolution = pio.read_json("figuras/trx_evo/transactions_evolution.json")
fig_fraud_unbiased_perc = pio.read_json("figuras/trx_evo/fraud_unbiased_perc.json")

fig_weekday_unbiased = pio.read_json("figuras/tempo/weekday_unbiased.json")
fig_time_evolution = pio.read_json("figuras/tempo/time_evolution.json")

fig_ratio_fraud = pio.read_json("figuras/amount/ratio_fraud.json")
fig_violin_breakdown = pio.read_json("figuras/amount/violin_breakdown.json")

fig_client_228_temporal = pio.read_json("figuras/client/client_228_temporal.json")
fig_client_228_mcc = pio.read_json("figuras/client/client_228_mcc.json")

fig_client_228_spatial = pio.read_json("figuras/spatial/client_228_spatial.json")
fig_rate_USAstates_fraud_unbiased = pio.read_json("figuras/spatial/rate_USAstates_fraud_unbiased.json")

fig_rf_1 = pio.read_json("figuras/mldl/rf_1.json")
fig_rf_2 = pio.read_json("figuras/mldl/rf_2.json")
fig_xgb_1 = pio.read_json("figuras/mldl/xgb_1.json")
fig_xgb_2 = pio.read_json("figuras/mldl/xgb_2.json")
fig_lgb_1 = pio.read_json("figuras/mldl/lgb_1.json")
fig_lgb_2 = pio.read_json("figuras/mldl/lgb_2.json")

fig_mlp_1 = pio.read_json("figuras/mldl/mlp_1.json")
fig_mlp_2 = pio.read_json("figuras/mldl/mlp_2.json")
fig_cnn_1 = pio.read_json("figuras/mldl/cnn_1.json")
fig_cnn_2 = pio.read_json("figuras/mldl/cnn_2.json")
fig_cnn_lstm_1 = pio.read_json("figuras/mldl/cnn_lstm_1.json")
fig_cnn_lstm_2 = pio.read_json("figuras/mldl/cnn_lstm_2.json")

## Creamos el dashboard
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H1("Financial Fraud Data Analysis", className="text-center mt-4 mb-4 fs-3", style={'fontWeight': 'bold'}),
            width=12
        )
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Tabs([

                dbc.Tab(
                    label="📊 Demography & Merchant",
                    tab_id="tab-demographic",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_demographic, id="graph-demographic")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_mcc_log2RF, id="graph-mcc_log2RF")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="📈 Transaction History",
                    tab_id="tab-history",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_transactions_evolution, id="graph-transactions_evolution")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_fraud_unbiased_perc, id="graph-fraud_unbiased_perc")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="🕒 Timing & Frequency",
                    tab_id="tab-temporal",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_weekday_unbiased, id="graph-weekday_unbiased")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_time_evolution, id="graph-time_evolution")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="💵 Amount & Payment",
                    tab_id="tab-amount",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_ratio_fraud, id="graph-ratio_fraud")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_violin_breakdown, id="graph-violin_breakdown")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="👤 Client Behaviour",
                    tab_id="tab-client",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_client_228_temporal, id="graph-client_228_temporal")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_client_228_mcc, id="graph-client_228_mcc")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="🌎 Fraud Mapping",
                    tab_id="tab-spatial",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_rate_USAstates_fraud_unbiased, id="graph-rate_USAstates_fraud_unbiased")
                            ], width=12, lg=6),
                            dbc.Col([
                                dcc.Graph(figure=fig_client_228_spatial, id="graph-client_228_spatial")
                            ], width=12, lg=6),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="🤖 Machine Learning",
                    tab_id="tab-ml",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_rf_1, id="graph-rf_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_xgb_1, id="graph-xgb_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_lgb_1, id="graph-lgb_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_rf_2, id="graph-rf_2")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_xgb_2, id="graph-xgb_2")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_lgb_2, id="graph-lgb_2")
                            ], width=12, lg=4),
                        ], className="align-items-center")
                    ]
                ),

                dbc.Tab(
                    label="🧠 Deep Learning",
                    tab_id="tab-dl",
                    className="p-3 bg-transparent",
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(figure=fig_mlp_1, id="graph-mlp_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_cnn_1, id="graph-cnn_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_cnn_lstm_1, id="graph-cnn_lstm_1")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_mlp_2, id="graph-mlp_2")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_cnn_2, id="graph-cnn_2")
                            ], width=12, lg=4),
                            dbc.Col([
                                dcc.Graph(figure=fig_cnn_lstm_2, id="graph-cnn_lstm_2")
                            ], width=12, lg=4),
                        ], className="align-items-center")
                    ]
                ),

            ], id="tabs-dashboard", active_tab="tab-client")
        ], width=12)
    ])

], fluid=True, className="px-4 py-2")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050, debug=True)
