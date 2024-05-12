import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

g_Helper.hookEvent(window, "load", false, () =>
{
	const control_div = document.querySelector("#controls > div")
	if (!g_Helper.isValidElement(control_div)) return // TODO: Error

	g_Builder.start(control_div)
	{
		switch (document.body.g_SessionData.user_type)
		{
			case "CUSTOMER":
			{
				// Does this need anything?

				break
			}

			case "VENDOR":
			{
				g_Builder.startElement("input")
				{
					g_Builder.addClass("flex_fill")

					g_Builder.setAttribute("type", "button")

					g_Builder.setProperty("value", "Edit Products")
				}
				g_Builder.endElement()

				break
			}

			case "ADMIN":
			{
				g_Builder.startElement("input")
				{
					g_Builder.addClass("flex_fill")

					g_Builder.setAttribute("type", "button")

					g_Builder.setProperty("value", "Edit Products")
				}
				g_Builder.endElement()

				// TODO: Accounts

				break
			}
		}
	}
	g_Builder.end()
})
