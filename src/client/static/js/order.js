import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_OrderData = {}
var g_ItemList = []
var g_ItemPrices = {}

const g_CurrencyFormatter = Intl.NumberFormat("en-US", {
	"style": "currency",
	"currency": "USD"
})

function displayOrder()
{
	const order_container = document.querySelector("#order_details > div")
	if (!g_Helper.isValidElement(order_container)) return // TODO: Error

	const order_table = order_container.querySelector("table")
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
					// TODO: Image?

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
					g_Builder.setProperty("innerHTML", g_CurrencyFormatter.format(g_ItemPrices[productData.id]))
				}
				g_Builder.endElement()
			}
			g_Builder.endElement()
		}
	}
	g_Builder.end()

	g_Builder.start(order_container)
	{
		g_Builder.startElement("div")
		{
			g_Builder.addClass("flexbox")
			g_Builder.addClass("flex_hspace")
			g_Builder.addClass("flex_vcenter")

			g_Builder.startElement("input")
			{
				g_Builder.setAttribute("type", "button")

				g_Builder.setProperty("value", "Print")

				// TODO: Print functionality
			}
			g_Builder.endElement()

			g_Builder.startElement("div")
			{
				g_Builder.addClass("flexbox")
				g_Builder.addClass("flex_column")

				g_Builder.startElement("h3")
				{
					g_Builder.addClass("float_right")

					g_Builder.setProperty("innerHTML", g_CurrencyFormatter.format(g_OrderData.price))
				}
				g_Builder.endElement()

				g_Builder.startElement("p")
				{
					g_Builder.setProperty("innerHTML", `Order Status: ${g_OrderData.status}`)
				}
				g_Builder.endElement()
			}
			g_Builder.endElement()
		}
		g_Builder.endElement()
	}
	g_Builder.end()
}

g_Helper.hookEvent(window, "load", false, () =>
{
	g_OrderData = fixJSONList(ORDER_DATA)
	g_ItemList = fixJSONList(ORDER_ITEMS)
	g_ItemPrices = JSON.parse(ITEM_PRICES)

	displayOrder()
})
