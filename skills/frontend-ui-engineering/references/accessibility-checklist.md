# Accessibility Checklist

Use this checklist selectively when the affected UI behavior makes the corresponding question material. Project standards, existing components, and the actual user flow outrank generic examples.

## Semantics And Names

- [ ] Native elements express the control or landmark where they fit.
- [ ] Interactive controls have a visible or equivalent accessible name.
- [ ] Images have useful alternatives, or are explicitly decorative.
- [ ] Headings, lists, tables, labels, and relationships match the content structure.
- [ ] Links navigate and buttons act; a non-semantic element is not used as a substitute without a demonstrated need.

## Keyboard And Focus

- [ ] Every affected interaction is reachable and operable with the supported keyboard input.
- [ ] Focus order follows the interaction flow and focus remains visible.
- [ ] Custom menus, dialogs, popovers, and other widgets have the project-required keyboard behavior.
- [ ] An overlay does not strand focus; when the project behavior requires it, focus returns to the invoking control on close.
- [ ] No interaction introduces an unintended keyboard trap.

## State, Forms, And Feedback

- [ ] Loading, empty, success, disabled, unavailable, and error states are meaningful for the affected flow.
- [ ] Form fields have associated labels, useful instructions, and errors that identify the affected field or summary.
- [ ] Dynamic status changes are perceivable without relying on color or timing alone.
- [ ] Validation, permission, and destructive-action feedback is understandable and actionable.

## Visual And Responsive Use

- [ ] Text, controls, and important graphics meet the project's contrast and visual-clarity standard.
- [ ] Color is not the only signal for status, error, selection, or difference.
- [ ] Content remains usable under the project's supported viewport, zoom, and text-size conditions.
- [ ] Touch targets, spacing, motion, and flashing follow the project's applicable standards and content needs.
- [ ] Existing design tokens and components are reused instead of introducing arbitrary values or a generic visual recipe.

## Evidence Selection

- [ ] Use static inspection or an existing focused test when it directly proves the claim.
- [ ] Use an existing project accessibility check only after inspecting its command and effects.
- [ ] Request or hand off live browser, screen-reader, or visual evidence only when the claim requires it and the runtime/tool boundary is available and authorized.
- [ ] Record unsupported runtime or tool-dependent claims as `UNVERIFIED`; do not turn this checklist into a blanket all-tools gate.
