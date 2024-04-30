import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"
import { Enum } from "./JSModules/enum.js"

export const APPEAR_DIRECTION = new Enum([ "LEFT", "RIGHT", "TOP", "BOTTOM" ])

export class ToolTip
{
	constructor()
	{
		const helper = Helper.assignToObject(this)
		this.m_Builder = new DOMBuilder()

		this.m_strText = "Hello"

		// Dumb
		const fixer = () => { ToolTip.fixLocations() }

		helper.hookEvent(window, "resize", true, fixer)
		helper.hookEvent(document, "scroll", true, fixer)
	}

	static fixLocations()
	{
		const helper = new Helper()
		const tooltips = document.querySelectorAll(".tooltip")

		tooltips.forEach((tooltip) =>
		{
			const tooltipRect = helper.getElementRect(tooltip)
			const elementRect = helper.getElementRect(tooltip.m_Element)

			switch (tooltip.m_iDirection)
			{
				default:
				case APPEAR_DIRECTION.LEFT:
				{
					tooltip.style.left = `${elementRect.x - tooltipRect.width}px`
					tooltip.style.top = `${(elementRect.y + (elementRect.height / 2)) - (tooltipRect.height / 2)}px`

					// Offset for ::before element
					tooltip.style.left = `calc(${tooltip.style.left} - 0.75em)`

					break
				}

				case APPEAR_DIRECTION.RIGHT:
				{
					tooltip.style.left = `${elementRect.x + elementRect.width}px`
					tooltip.style.top = `${(elementRect.y + (elementRect.height / 2)) - (tooltipRect.height / 2)}px`

					tooltip.style.left = `calc(${tooltip.style.left} + 0.75em)`

					break
				}

				case APPEAR_DIRECTION.TOP:
				{
					tooltip.style.left = `${(elementRect.x + (elementRect.width / 2)) - (tooltipRect.width / 2)}px`
					tooltip.style.top = `${elementRect.y - tooltipRect.height}px`

					tooltip.style.top = `calc(${tooltip.style.top} - 0.75em)`

					break
				}

				case APPEAR_DIRECTION.BOTTOM:
				{
					tooltip.style.left = `${(elementRect.x + (elementRect.width / 2)) - (tooltipRect.width / 2)}px`
					tooltip.style.top = `${elementRect.y + elementRect.height}px`

					tooltip.style.top = `calc(${tooltip.style.top} + 0.75em)`

					break
				}
			}
		})
	}

	getText()
	{
		return this.m_strText
	}

	setText(text)
	{
		this.m_strText = this.getHelper().getString(text, "Hello")
	}

	construct(element, direction)
	{
		const builder = this.m_Builder
		var constructed = null

		builder.start()
		{
			constructed = builder.startElement("div")
			{
				builder.addClasses([
					"tooltip",

					"flexbox",
					"flex_vcenter"
				])

				builder.setAttribute("direction", APPEAR_DIRECTION.translateValue(direction))

				builder.setProperty("m_Element", element)
				builder.setProperty("m_iDirection", direction)

				builder.startElement("p")
				{
					builder.setProperty("innerHTML", this.getText())
				}
				builder.endElement()
			}
			builder.endElement()
		}
		builder.end()

		return constructed
	}

	appear(element, direction)
	{
		const helper = this.getHelper()

		if (!helper.isValidElement(element))
			throw new Error("Invalid element in appear")

		this.construct(element, direction)

		ToolTip.fixLocations()
	}

	hide(element)
	{
		const helper = this.getHelper()

		if (!helper.isValidElement(element))
			throw new Error("Invalid element in hide")

		const tooltips = document.querySelectorAll(".tooltip")

		tooltips.forEach((tooltip) =>
		{
			if (tooltip.m_Element == element)
				tooltip.remove()
		})
	}
}
