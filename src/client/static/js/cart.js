import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_ItemList = []

function updateCartList()
{
	const cart_grid = document.querySelector("#cart_grid")
	if (!g_Helper.isValidElement(cart_grid)) return // TODO: Error

	g_Builder.start(cart_grid)
	{
		for (const item of g_ItemList)
		{
			g_Builder.startElement("div")
			{
				g_Builder.addClass("flexbox")
				g_Builder.addClass("flex_vcenter")
				g_Builder.addClass("flex_hspace")
				g_Builder.addClass("flex_fill")

				g_Builder.startElement("div")
				{
					g_Builder.setProperty("innerHTML", item.product_id)
				}
				g_Builder.endElement()
			}
			g_Builder.endElement()
		}
	}
	g_Builder.end()
}

g_Helper.hookEvent(window, "load", false, () =>
{
	g_ItemList = fixJSONList(CART_ITEMS)

	console.log(g_ItemList)

	updateCartList()
})
