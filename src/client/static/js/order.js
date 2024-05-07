import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_OrderData = {}
var g_ItemList = []

const g_CurrencyFormatter = Intl.NumberFormat("en-US", {
	"style": "currency",
	"currency": "USD"
})

function displayOrder()
{
	const order_table = document.querySelector("#order_details table")
	if (!g_Helper.isValidElement(order_table)) return // TODO: Error

	g_Builder.start(order_table)
	{
		for (const item of g_ItemList)
		{
			const productData = item.product
			if (!productData) continue // TODO: Error

			g_Builder.startElement("tr")
			{
				g_Builder.startElement("td")
				{
					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_column")

						g_Builder.startElement("h3")
						{
							g_Builder.setProperty("innerHTML", productData.name)
						}
						g_Builder.endElement()

						g_Builder.startElement("p")
						{
							g_Builder.setProperty("innerHTML", `Order Quantity: ${item.quantity}`)
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()
				}
				g_Builder.endElement()

				g_Builder.startElement("td")
				{
					g_Builder.setProperty("innerHTML", g_CurrencyFormatter.format(productData.price))
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
	g_OrderData = fixJSONList(ORDER_DATA)
	g_ItemList = fixJSONList(ORDER_ITEMS)

	displayOrder()
})
