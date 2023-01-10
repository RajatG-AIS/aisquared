from aisquared.base import BaseObject


class PieChartRendering(BaseObject):
    """
    Rendering class for rendering a Pie Chart

    Example usage:

    >>> import aisquared
    >>> my_obj = aisquared.config.rendering.PieChartRendering(
        'my pie chart',
        'MyPieChartID',
        'MyPieChart',
        ['red', 'blue'],
        ['label1', 'label2'],
        'my_countainer_id',
        'key',
        'value',
        'name',
        True,
        'circle'
    )
    >>> my_obj.to_dict()
    {'className': 'PieChartRendering',
    'label': 'my pie chart',
    'params': {'id': 'MyPieChartID',
    'chartName': 'MyPieChart',
    'chartColors': ['red', 'blue'],
    'chartLabels': ['label1', 'label2'],
    'containerId': 'my_countainer_id',
    'predictionNameKey': 'key',
    'predictionValueKey': 'value',
    'predictionNameValue': 'name',
    'displayLegend': True,
    'legendIcon': 'circle',
    'width': 'auto',
    'height': 'auto',
    'xOffset': '0',
    'yOffset': '0'}}

    """

    def __init__(
        self,
        label: str,
        id: str,
        chart_name: str,
        chart_colors: list,
        chart_labels: list,
        container_id: str,
        prediction_name_key: str,
        prediction_value_key: str,
        prediction_name_value: str,
        display_legend: bool,
        legend_icon: str,
        width: str = 'auto',
        height: str = 'auto',
        xOffset: str = '0',
        yOffset: str = '0',

    ):
        """
        Parameters
        ----------
        label : str
            The label for the chart
        id : str
            The ID for the chart
        chart_name : str
            The name for the chart
        chart_colors : list of str
            List of colors to use
        chart_labels : list of str
            List of labels to use
        container_id : str
            The ID of the container to use
        prediction_name_key : str
            The key to use for the prediction name
        prediction_value_key : str
            The key to use for the prediction value
        prediction_name_value : str
            The value to use for the prediction name
        display_legend : bool
            Whether to display the chart legend
        legend_icon : str
            The legend icon to display
        width : str (default 'auto')
            The width of the chart
        height : str (default 'auto')
            The height of the chart
        xOffset : str (default '0')
            The offset on the x axis
        yOffset : str (default '0')
            The offset on the y axis
        """
        super().__init__()
        self.label = label
        self.id = id
        self.chart_name = chart_name
        self.chart_colors = chart_colors
        self.chart_labels = chart_labels
        self.container_id = container_id
        self.prediction_name_key = prediction_name_key
        self.prediction_value_key = prediction_value_key
        self.prediction_name_value = prediction_name_value
        self.display_legend = display_legend
        self.legend_icon = legend_icon
        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset

    def to_dict(self) -> dict:
        """
        Get the configuration object as a dictionary
        """
        return {
            'className': 'PieChartRendering',
            'label': self.label,
            'params': {
                'id': self.id,
                'chartName': self.chart_name,
                'chartColors': self.chart_colors,
                'chartLabels': self.chart_labels,
                'containerId': self.container_id,
                'predictionNameKey': self.prediction_name_key,
                'predictionValueKey': self.prediction_value_key,
                'predictionNameValue': self.prediction_name_value,
                'displayLegend': self.display_legend,
                'legendIcon': self.legend_icon,
                'width': self.width,
                'height': self.height,
                'xOffset': self.xOffset,
                'yOffset': self.yOffset
            }
        }