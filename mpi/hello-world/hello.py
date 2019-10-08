from mpi4py import MPI

communicator = MPI.COMM_WORLD

size = communicator.Get_size()
rank = communicator.Get_rank()

print(f"I am rank {rank} in group of {size} processes.")
