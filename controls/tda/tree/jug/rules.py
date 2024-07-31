from controls.tda.list.linked_list import Linked_List
from controls.tda.tree.jug.node_jug import NodeJug


class Rules:

    def rules(self, jb, jl):
        rules = Linked_List()
        x = jb._current_capacity
        y = jl._current_capacity

        # 1. Llenar jarra grande completamente
        if y < jb._capacity:
            new_node = NodeJug()
            new_node.set_current_capacity(jb._capacity, y)
            rules.add(new_node)
            print("Regla 1: Llenar jarra grande completamente")

        # 2. Llenar jarra pequeña completamente
        if x < jl._capacity:
            new_node = NodeJug()
            new_node.set_current_capacity(x, jl._capacity)
            rules.add(new_node)
            print("Regla 2: Llenar jarra pequeña completamente")

        # 3. Vaciar jarra grande completamente
        if x > 0:
            new_node = NodeJug()
            new_node.set_current_capacity(0, y)
            rules.add(new_node)
            print("Regla 3: Vaciar jarra grande completamente")

        # 4. Vaciar jarra pequeña completamente
        if y > 0:
            new_node = NodeJug()
            new_node.set_current_capacity(x, 0)
            rules.add(new_node)
            print("Regla 4: Vaciar jarra pequeña completamente")

        # 5. Llenar jarra grande con la jarra pequeña
        if (x + y) >= jb._capacity and (x < jb._capacity and y > 0):
            new_node = NodeJug()
            new_node.set_current_capacity(jb._capacity, y - (jb._capacity - x))
            rules.add(new_node)
            print("Regla 5: Llenar jarra grande con la jarra pequeña")

        # 6. Llenar jarra pequeña con la jarra grande
        if (x + y) >= jl._capacity and (x > 0 and y < jl._capacity):
            new_node = NodeJug()
            new_node.set_current_capacity(x - (jl._capacity - y), jl._capacity)
            rules.add(new_node)
            print("Regla 6: Llenar jarra pequeña con la jarra grande")

        # 7. Vaciar jarra grande en la jarra pequeña
        if (x + y) <= jl._capacity and (x > 0 and y < jl._capacity):
            new_node = NodeJug()
            new_node.set_current_capacity(0, x + y)
            rules.add(new_node)
            print("Regla 7: Vaciar jarra grande en la jarra pequeña")

        # 8. Vaciar jarra pequeña en la jarra grande
        if (x + y) <= jb._capacity and (x < jb._capacity and y > 0):
            new_node = NodeJug()
            new_node.set_current_capacity(x + y, 0)
            rules.add(new_node)
            print("Regla 8: Vaciar jarra pequeña en la jarra grande")

        return rules
