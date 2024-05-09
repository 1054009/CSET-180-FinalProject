import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

g_Helper.hookEvent(window, "load", false, () =>
{
	const control_div = document.querySelector("#controls > div")
	if (!g_Helper.isValidElement(control_div)) return // TODO: Error

	switch (document.body.g_SessionData.user_type)
	{
		case "CUSTOMER":
		{
			break
		}

		case "VENDOR":
		{
			break
		}

		case "ADMIN":
		{
			break
		}
	}
})
