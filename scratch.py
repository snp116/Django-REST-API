
@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only Manager should see this"})
    else:
        return Response({"message": "You are not authorized"}, 403)




# @api_view(['GET','POST'])
# def menu_items(request):
#     ordering_fields = ['price', 'inventory']
#     filterset_fields = ['price', 'inventory']
#     search_fields = ['title']
#     if(request.method=='GET'):
#         items = MenuItem.objects.select_related('category').all()
#         category_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         if category_name:
#             items = items.filter(category__title=category_name)
#         if to_price:
#             items = items.filter(price=to_price)
#         serialized_item = MenuItemSerializer(items, many=True)
#         return Response(serialized_item.data)
#     elif(request.method=='POST'):
#         serialized_item = MenuItemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
#         return Response(serialized_item.validated_data,status.HTTP_201_CREATED)