import React from "react"
import { reducer, initialState } from "./reducer"

export const StationsContext = React.createContext({
  state: initialState,
  dispatch: () => null
})

export const StationsProvider = ({ children }) => {
  const [state, dispatch] = React.useReducer(reducer, initialState)

  return (
    <StationsContext.Provider value={[ state, dispatch ]}>
    	{ children }
    </StationsContext.Provider>
  )
}