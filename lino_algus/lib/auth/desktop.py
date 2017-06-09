# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

"""Desktop UI for this plugin.

"""

from lino.api import dd, _

from lino.modlib.auth.desktop import *

class UserDetail(UserDetail):
    """Layout of User Detail in Lino Algus."""

    main = "general contact"

    general = dd.Panel("""
    box1
    remarks:40 auth.AuthoritiesGiven:20
    """, label=_("General"))

    box1 = """
    username profile:20
    language timezone
    id created modified
    """

    contact = dd.Panel("""
    first_name last_name initials
    place
    lets.DemandsByUser lets.OffersByUser
    """, label=_("Contact"))

Users.detail_layout = UserDetail()

Users.column_names = "first_name email place offered_products wanted_products"
