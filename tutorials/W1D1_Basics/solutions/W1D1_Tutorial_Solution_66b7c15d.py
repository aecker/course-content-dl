
def functionA(A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
  ## TODO for students
  output = A.sum(axis = 0) * B.sum()
  return output

def functionB(C: torch.Tensor) -> torch.Tensor:


  # TODO flatten the tensor  C
  C = C.flatten()

  # TODO create the idx tensor to be concatenated to C

  # here we're going to do flatten and unsqueeze, but reshape can also be used
  idx_tensor = torch.arange(0, len(C))

  # TODO concatenate the two tensors
  output = torch.cat([idx_tensor.unsqueeze(0), C.unsqueeze(0)], axis = 1)

  return output

def functionC(D: torch.Tensor, E: torch.Tensor) -> torch.Tensor:

  # TODO check we can reshape E into the shape of D
  if torch.numel(D) == torch.numel(E) :
    # TODO reshape E into the shape of D
    E = E.reshape(D.shape)

    # TODO sum the two tensors
    output = D + E

  else:
    # TODO flatten both tensors
    # this time we'll use reshape to keep the singleton dimension
    D = D.reshape(1,-1)
    E = E.reshape(1,-1)

    # TODO concatenate the two tensors in the correct dimension
    output = torch.cat([D,E], axis = 1)

  return output

print(functionA(torch.tensor([[1,1], [1,1]]), torch.tensor([ [1,2,3],[1,2,3] ]) ))
print(functionB(torch.tensor([ [2,3],[-1,10] ])))
print(functionC(torch.tensor([[1, -1],[-1,3]]), torch.tensor([[2,3,0,2]])))
print(functionC(torch.tensor([[1, -1],[-1,3]]), torch.tensor([[2,3,0]])))