import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_ProductList = []
var g_ImageList = []

const g_CurrencyFormatter = Intl.NumberFormat("en-US", {
	"style": "currency",
	"currency": "USD"
})

function getProductImages(id)
{
	const images = []

	for (const imageData of g_ImageList)
	{
		if (imageData.product_id == id)
			images.push(imageData.image_data)
	}

	return images
}

function updateProductDisplay()
{
	const product_grid = document.querySelector("#product_grid")
	if (!g_Helper.isValidElement(product_grid)) return // TODO: Error

	const hasValidSession = document.body.g_bSessionIsValid

	g_Builder.start(product_grid)
	{
		g_Builder.setProperty("innerHTML", "")

		for (const productData of g_ProductList)
		{
			g_Builder.startElement("div")
			{
				g_Builder.addClass("upper_glow")

				g_Builder.startElement("div")
				{
					g_Builder.addClass("product_card")
					g_Builder.addClass("flexbox")
					g_Builder.addClass("flex_column")
					g_Builder.addClass("flex_gap")

					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_hcenter")
						g_Builder.addClass("flex_vcenter")

						g_Builder.startElement("div")
						{
							g_Builder.addClass("product_image")
							g_Builder.addClass("flexbox")
							g_Builder.addClass("flex_hcenter")
							g_Builder.addClass("flex_vcenter")

							g_Builder.startElement("img")
							{
								g_Builder.setProperty("src", getProductImages(productData.id)[0])
							}
							g_Builder.endElement()
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()

					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_column")

						g_Builder.startElement("div")
						{
							g_Builder.addClass("flexbox")
							g_Builder.addClass("flex_hspace")

							g_Builder.startElement("h3")
							{
								g_Builder.setProperty("innerHTML", productData.name)
							}
							g_Builder.endElement()

							g_Builder.startElement("h4")
							{
								g_Builder.setProperty("innerHTML", g_CurrencyFormatter.format(productData.price))
							}
							g_Builder.endElement()
						}
						g_Builder.endElement()

						g_Builder.startElement("div")
						{
							g_Builder.addClass("flexbox")
							g_Builder.addClass("flex_hspace")

							g_Builder.startElement("p")
							{
								g_Builder.setProperty("innerHTML", productData.description)
							}
							g_Builder.endElement()

							g_Builder.startElement("p")
							{
								g_Builder.setProperty("innerHTML", `${productData.inventory} in stock`)
							}
							g_Builder.endElement()
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()

					g_Builder.startElement("div")
					{
						g_Builder.addClass("flexbox")
						g_Builder.addClass("flex_hcenter")

						g_Builder.startElement("input")
						{
							g_Builder.setAttribute("type", "button")

							if (!hasValidSession)
								g_Builder.setProperty("disabled", true)

							g_Builder.setProperty("value", "Add to Cart")

							// TODO: Add to cart functionality
						}
						g_Builder.endElement()
					}
					g_Builder.endElement()
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
	g_ImageList = fixJSONList(PRODUCT_IMAGES)
	console.log(g_ProductList)
	console.log(g_ImageList)

	updateProductDisplay()
})
