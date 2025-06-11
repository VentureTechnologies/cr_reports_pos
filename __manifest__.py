# -*- coding: utf-8 -*-
# -*- develop by: jartavia05 -*-
{
    'name': "Reporte IVA Costa Rica POS",
    'summary': "Reportes POS para IVA en Costa Rica.",
    'description': """
Este reporte esta diseñado para generar un informe simple y fácil para la facturación electronica de Costa Rica.
Añade los siguientes campos al reporte de órdenes de punto de venta (report.pos.order):
        - Monto de Impuesto por Línea: El impuesto correspondiente a cada línea de pedido.
        - Total de Impuesto por Orden: Suma total de los impuestos para una orden completa, visible al agrupar.
    """,

    'author': "Venture Technology",
    'website': "https://www.venturetech.site",
    'category': 'Invoicing Management',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_order_report_views.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

