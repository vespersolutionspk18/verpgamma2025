import unittest

import frappe

from verp import encode_company_abbr

test_records = frappe.get_test_records("Company")


class TestInit(unittest.TestCase):
	def test_encode_company_abbr(self):
		abbr = "NFECT"

		names = [
			"Warehouse Name",
			"VERP Foundation India",
			f"Gold - Member - {abbr}",
			f" - {abbr}",
			"VERP - Foundation - India",
			f"VERP Foundation India - {abbr}",
			f"No-Space-{abbr}",
			"- Warehouse",
		]

		expected_names = [
			f"Warehouse Name - {abbr}",
			f"VERP Foundation India - {abbr}",
			f"Gold - Member - {abbr}",
			f" - {abbr}",
			f"VERP - Foundation - India - {abbr}",
			f"VERP Foundation India - {abbr}",
			f"No-Space-{abbr} - {abbr}",
			f"- Warehouse - {abbr}",
		]

		for i in range(len(names)):
			enc_name = encode_company_abbr(names[i], abbr=abbr)
			self.assertTrue(
				enc_name == expected_names[i],
				f"{enc_name} is not same as {expected_names[i]}",
			)

	def test_translation_files(self):
		from frappe.tests.test_translate import verify_translation_files

		verify_translation_files("verp")

	def test_patches(self):
		from frappe.tests.test_patches import check_patch_files

		check_patch_files("verp")
