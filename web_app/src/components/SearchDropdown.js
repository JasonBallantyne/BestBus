import { useQuery, gql } from "@apollo/client";
import { useState } from "react";

const CUSTOMERS = gql`
  query GetCustomers {
    allCustomers {
      name
      gender
      id
    }
  }
`;

function SearchDropdown(endpoint) {

  const { loading, error, data } = useQuery(CUSTOMERS);
  const [nameSearch, setNameSearch] = useState('');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      <input type="text" placeholder="Search by stop number" onChange={event => {setNameSearch(event.target.value)}} />
      { data.allCustomers.filter((val)=> {
        if (nameSearch === "") {
          return val
        } else if (val.name.toLowerCase().includes(nameSearch.toLowerCase())) {
          return val
        } else {
          return null
        }
      }).map(({ name, gender, id }) => {
        return (
          <div key={id}>
            <p>
              {name}: {gender}
            </p>
          </div>
        )
      })}
    </div>
  )
}

export default SearchDropdown;