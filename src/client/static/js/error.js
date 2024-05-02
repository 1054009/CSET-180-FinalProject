import { Helper } from "./JSModules/helper.js"
import { APPEAR_DIRECTION, ToolTip } from "./tooltip.js"

const g_Helper = new Helper()
const g_ToolTipManager = new ToolTip()

g_Helper.hookEvent(window, "load", false, () =>
{
	if (g_Helper.isString(TOOLTIP_ELEMENT) && TOOLTIP_ELEMENT.length > 0)
	{
		const element = document.querySelector(TOOLTIP_ELEMENT) || document.body
		const text = TOOLTIP_TEXT || "Something went wrong"
		const direction = g_Helper.getNumber(TOOLTIP_DIRECTION, false, APPEAR_DIRECTION.LEFT)

		g_ToolTipManager.hide(element)
		g_ToolTipManager.setText(text)
		g_ToolTipManager.appear(element, direction)
	}
})
