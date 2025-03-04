{
    'name': 'Clinica Veterinaria',
    'version': '1.0.0',
    'author': 'Fernando',
    'category': 'Veterinaria',
    'license': 'LGPL-3',
    'summary': 'Un módulo que administra una veterinaria.',
    'description': """
        Este es un módulo para administrar personas, mascotas, veterinarios y citas médicas.
    """,
    'depends': ['base', 'contacts'],  # 'contacts' asegura que 'res.partner' esté disponible
    'data': [
        'security/ir.model.access.csv',
        'views/vet_mascota_views.xml',  # Asegúrate de incluir este archivo
        'views/res_partner_vet_views.xml',  # Asegúrate de incluir este archivo
        'views/vet_cita_views.xml',  
        'views/vet_menus.xml',  # Asegúrate de incluir este archivo

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}