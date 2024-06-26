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

	// TODO: Show message when cart is empty
	g_Builder.start(cart_grid)
	{
		for (const item of g_ItemList)
		{
			const productData = item.product
			if (!productData) continue // TODO: Error

			productData.images = fixJSONList(productData.images)

			g_Builder.startElement("div")
			{
				g_Builder.addClass("upper_glow")

				g_Builder.startElement("div")
				{
					g_Builder.addClass("cart_item")
					g_Builder.addClass("flexbox")
					g_Builder.addClass("flex_vcenter")
					g_Builder.addClass("flex_hspace")
					g_Builder.addClass("flex_fill")

					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_vcenter")
						g_Builder.addClass("flex_gap")
						g_Builder.addClass("flex_fill")

						// TODO: Image background
						// TODO: Fix when no image
						const imageObject = productData.images[0]
						if (imageObject)
						{
							g_Builder.startElement("img")
							{
								g_Builder.setProperty("src", imageObject.image_data)
							}
							g_Builder.endElement()
						}

						g_Builder.startElement("h4")
						{
							g_Builder.setProperty("innerHTML", productData.name)
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()

					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_vcenter")
						g_Builder.addClass("flex_fill")

						g_Builder.startElement("p")
						{
							g_Builder.setProperty("innerHTML", `${item.quantity} in cart`)

							// TODO: Ability to change amount in cart
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()

					g_Builder.startElement("form")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_vcenter")
						g_Builder.addClass("flex_fill")

						g_Builder.startElement("input")
						{
							g_Builder.addClass("float_right")

							g_Builder.setAttribute("type", "submit")

							g_Builder.setProperty("value", "Remove")

							// TODO: Functionality to remove
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()
				}
				g_Builder.endElement()
			}
			g_Builder.endElement()
		}

		g_Builder.startElement("form")
		{
			g_Builder.setAttribute("action", "/cart/place_order")
			g_Builder.setAttribute("method", "POST")

			g_Builder.setProperty("style.paddingRight", "1em")

			g_Builder.startElement("input")
			{
				g_Builder.addClass("float_right")

				g_Builder.setAttribute("type", "submit")

				g_Builder.setProperty("value", "Place order")
			}
			g_Builder.endElement()
		}
		g_Builder.endElement()
	}
	g_Builder.end()
}

g_Helper.hookEvent(window, "load", false, () =>
{
	g_ItemList = fixJSONList(CART_ITEMS)

	updateCartList()
})
