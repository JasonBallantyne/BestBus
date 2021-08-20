export const reducer = (state, action) => {
  switch (action.type) {
    case "update_stations":
      return action.payload

    default:
      return state
  }
}

export const initialState = null