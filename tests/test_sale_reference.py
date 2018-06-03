# This file is part of the sale_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_teardown, doctest_checker


class SaleReferenceTestCase(ModuleTestCase):
    'Test Sale Reference module'
    module = 'sale_reference'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleReferenceTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_sale_reference.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
            checker=doctest_checker))
    return suite
