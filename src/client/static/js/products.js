import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_ProductList = []

function updateProductDisplay()
{
	const product_grid = document.querySelector("#product_grid")
	if (!g_Helper.isValidElement(product_grid)) return // TODO: Error

	g_Builder.start(product_grid)
	{
		g_Builder.setProperty("innerHTML", "")

		for (const productData of g_ProductList)
		{
			g_Builder.startElement("div")
			{
				g_Builder.startElement("p")
				{
					g_Builder.setProperty("innerHTML", productData.name)
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
	g_ProductList = fixJSONList(PRODUCT_LIST)
	console.log(g_ProductList)

	updateProductDisplay()
})
