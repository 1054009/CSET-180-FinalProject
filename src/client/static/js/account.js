import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

g_Helper.hookEvent(window, "load", false, () =>
{
	const control_div = document.querySelector("#controls > div")
	if (!g_Helper.isValidElement(control_div)) return // TODO: Error

	console.log(document.body.g_SessionData)

	g_Builder.start(control_div)
	{
		switch (document.body.g_SessionData.user_type)
		{
			case "CUSTOMER":
			{
				break
			}

			case "VENDOR":
			{
				g_Builder.startElement("input")
				{
					g_Builder.setAttribute("type", "button")

					g_Builder.setProperty("value", "Add Product")
				}
				g_Builder.endElement()

				g_Builder.startElement("input")
				{
					g_Builder.setAttribute("type", "button")

					g_Builder.setProperty("value", "Delete Product")
				}
				g_Builder.endElement()

				g_Builder.startElement("input")
				{
					g_Builder.setAttribute("type", "button")

					g_Builder.setProperty("value", "Edit Product")
				}
				g_Builder.endElement()

				break
			}

			case "ADMIN":
			{
				break
			}
		}
	}
	g_Builder.end()
})
