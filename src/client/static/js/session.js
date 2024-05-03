import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

function addHeaderLink(text, iconName, url)
{
	g_Builder.startElement("li")
	{
		g_Builder.startElement("a")
		{
			g_Builder.addClass("flexbox")
			g_Builder.addClass("flex_vcenter")
			g_Builder.addClass("flex_gap_small")

			g_Builder.setAttribute("href", url)

			g_Builder.startElement("ion-icon")
			{
				g_Builder.setAttribute("name", iconName)
			}
			g_Builder.endElement()

			g_Builder.setProperty("innerHTML", `${g_Builder.getProperty("innerHTML")} ${text}`)
		}
		g_Builder.endElement()
	}
	g_Builder.endElement()
}

g_Helper.hookEvent(window, "load", false, () =>
{
	document.body.g_SessionData = SESSION // Make sure everyone can access it
	document.body.g_bSessionIsValid = SESSION.email_address != null

	// Setup navbar buttons
	const header = document.querySelector("header")

	if (g_Helper.isValidElement(header))
	{
		const headerList = header.querySelector("ul")

		if (headerList)
		{
			g_Builder.start(headerList)
			{
				addHeaderLink("Browse Products", "pricetag-outline", "/products/")

				if (document.body.g_bSessionIsValid)
				{
					addHeaderLink("View Cart", "cart-outline", "/cart/")
					addHeaderLink("Account", "person-circle-outline", "/account/")
				}
				else
				{
					addHeaderLink("Sign Up", "person-add-outline", "/signup/")
					addHeaderLink("Login", "log-in-outline", "/login/")
				}
			}
			g_Builder.end()
		}
	}
})
