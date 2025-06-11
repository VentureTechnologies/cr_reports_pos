# my_pos_reports/models/pos_order_report.py

from odoo import fields, models

class PosOrderReport(models.Model):
    _inherit = 'report.pos.order'

    # Campo calculado para el monto del impuesto en la LÍNEA del pedido
    # Mantener este campo es útil si quieres ver el impuesto línea por línea
    total_tax_amount = fields.Float(
        string='Impuesto',
        help="Monto total del impuesto del pedido de punto de venta, ya considerando descuentos."
    )
    subtotal_untaxed = fields.Float(
        string='Subotal Sin Impuesto',
        help="Monto subototal SIN impuesto, ya considerando descuentos"
    )


    # --- Método _select para añadir la columna al reporte SQL ---
    @property
    def _table_query(self):
        """ Sobreescribe el método para añadir nuestra columna de impuesto al SELECT de la vista SQL. """
        return f"""
            {self._select()}
            {self._from()}
            {self._group_by()}
        """

    def _select(self):
        """ Extiende la parte SELECT de la consulta SQL del reporte. """
        # Llama al _select original para obtener todas las columnas estándar del reporte.
        res = super()._select()

        # Añade nuestra nueva columna de impuesto.
        # report.pos.order internamente suma estos valores para cada línea de reporte.
        # price_subtotal_incl es el total con descuento para la línea agregada en el reporte.
        # price_sub_total es el subtotal sin descuento para la línea agregada en el reporte.

        res += """,
            (SUM(l.price_subtotal_incl) - SUM(l.price_subtotal)) AS total_tax_amount,
            SUM(ROUND((l.price_subtotal_incl) / CASE COALESCE(s.currency_rate, 0) WHEN 0 THEN 1.0 ELSE s.currency_rate END, cu.decimal_places))  - (SUM(l.price_subtotal_incl) - SUM(l.price_subtotal)) AS subtotal_untaxed
            
        """

        return res



